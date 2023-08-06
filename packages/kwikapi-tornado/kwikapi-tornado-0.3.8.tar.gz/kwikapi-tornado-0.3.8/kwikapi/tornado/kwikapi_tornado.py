# -*- coding: utf-8 -*

import asyncio
import gzip
import io

import tornado
import tornado.ioloop

from tornado.web import RequestHandler as TornadoRequestHandler
from tornado.web import asynchronous
from kwikapi import BaseRequest, BaseResponse, BaseRequestHandler
from requests.structures import CaseInsensitiveDict

from deeputil import Dummy

DUMMY_LOG = Dummy()


class TornadoRequest(BaseRequest):
    def __init__(self, req_hdlr):
        super().__init__()
        self._request = req_hdlr.request
        self.response = TornadoResponse(req_hdlr)

    @property
    def url(self):
        return self._request.uri

    @property
    def method(self):
        return self._request.method

    @property
    def body(self):
        return self._request.body

    @property
    def headers(self):
        return self._request.headers


class TornadoResponse(BaseResponse):
    def __init__(self, req_hdlr):
        super().__init__()
        self._req_hdlr = req_hdlr
        self._headers = CaseInsensitiveDict()

    def write(self, data, proto, stream=False):
        n, t = super().write(data, proto, stream=stream)

        if not stream:
            nbytes = n.value

            accept_enc = self._req_hdlr.request.headers.get("Accept-Encoding", "")
            accept_enc = set(
                [e.strip().lower() for e in accept_enc.split(",") if e.strip()]
            )

            if "gzip" in accept_enc:
                compressed = io.BytesIO()
                gfile = gzip.GzipFile(fileobj=compressed, mode="w")
                gfile.write(self._data)
                gfile.flush()
                gfile.close()
                self._data = compressed.getvalue()
                nbytes = len(self._data)
                self._headers["Content-Encoding"] = "gzip"

            self._headers["Content-Length"] = nbytes

        self._stream = stream

        return n, t

    def flush(self):
        pass

    def close(self):
        pass

    @property
    def headers(self):
        return self._headers


class RequestHandler(TornadoRequestHandler):
    PROTOCOL = BaseRequestHandler.DEFAULT_PROTOCOL

    def __init__(self, *args, **kwargs):
        self.api = kwargs.pop("api")
        self.log = kwargs.pop("log", DUMMY_LOG)

        default_version = kwargs.pop("default_version", None)
        default_protocol = kwargs.pop("default_protocol", self.PROTOCOL)

        pre_call_hook = kwargs.pop("pre_call_hook", None)
        post_call_hook = kwargs.pop("post_call_hook", None)

        self.kwik_req_hdlr = BaseRequestHandler(
            self.api,
            default_version=default_version,
            default_protocol=default_protocol,
            pre_call_hook=pre_call_hook,
            post_call_hook=post_call_hook,
            log=self.log,
        )

        super().__init__(*args, **kwargs)

    async def _handle(self):
        threadpool = self.api.threadpool

        def fn():
            req = TornadoRequest(self)
            self.kwik_req_hdlr.handle_request(req)
            return req.response

        try:
            if threadpool:
                loop = tornado.ioloop.IOLoop.current()
                res = await loop.run_in_executor(threadpool, fn)
            else:
                res = fn()

            for k, v in res.headers.items():
                self.set_header(k, v)

            if not res._stream:
                self.write(res._data)
                self.flush()
            else:

                for x in res._data:
                    self.write(x)
                    try:
                        await self.flush()
                    except tornado.iostream.StreamClosedError:
                        continue
        except Exception:
            self.log.exception("unhandle_request_handling_exception")
            raise
        finally:
            self.finish()

    get = post = _handle
