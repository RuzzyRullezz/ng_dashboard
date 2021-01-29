from __future__ import annotations

import traceback

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

from neopay_api.core.utils.datetimes import utc_now

from .context import LogContext


class LogMiddleware(BaseHTTPMiddleware):
    request_patched: bool = False

    @classmethod
    def patch_request_body(cls):
        if cls.request_patched:
            return

        body_original = Request.body

        async def body_patched(request: Request):
            body_content_key = 'body_content'
            body_content = request.scope.get(body_content_key)
            if body_content:
                return body_content
            body_content = await body_original(request)
            request.scope[body_content_key] = body_content
            return body_content

        Request.body = body_patched
        cls.request_patched = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.patch_request_body()

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        request_datetime = utc_now()
        exception_traceback = None
        response = None
        try:
            response = await call_next(request)
            return response
        except Exception:
            exception_traceback = traceback.format_exc()
            raise
        finally:
            response_datetime = utc_now()
            log_context = await LogContext.create(request_datetime, request, response_datetime,
                                                  response=response, exception_traceback=exception_traceback)
            await log_context.store()
