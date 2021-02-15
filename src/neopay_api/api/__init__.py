from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from neopay_api import config
from neopay_api.core.logging.incoming_request_log.middleware import LogMiddleware
from neopay_api.api import middlewares, errors, routing


def init_app():
    title = 'NEOPAY API'
    application = FastAPI(title=title)
    # middlwares
    application.add_middleware(CORSMiddleware, **middlewares.cors_middleware_params)
    application.add_middleware(LogMiddleware)
    # set exceptions handler
    application.add_exception_handler(errors.ApiErrorException, errors.api_error_exception_handler)
    # urls
    application.include_router(routing.root_router, prefix='/api')
    # return
    return application


config.setup_logging()
app = init_app()
