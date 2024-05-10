from fastapi import FastAPI, Header, responses

from src.service.config.settings import settings
from src.service.config.containers import Container

from src.service.entrypoints.routers import routes

DEBUG = eval(settings.FASTAPI_DEBUG)

def start_app():
    container = Container()

    app_ = FastAPI(
        title = settings.FASTAPI_TITLE,
        description = settings.FASTAPI_DESCRIPTION,
        debug = DEBUG,
        openapi_url=('/openapi.json' if DEBUG else None),
        docs_url=('/docs' if DEBUG else None),
        redoc_url=('/redocs' if DEBUG else None),
    )
    
    app_.include_router(routes.router)

    app_.openapi_version = "3.0.0"
    app_.container = container

    return app_

app = start_app()