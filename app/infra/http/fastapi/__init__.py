from fastapi import FastAPI

from app.settings import AppSettings
from app.infra.http.fastapi.handler.planning import planning_router


def create_app() -> FastAPI:
    application = FastAPI(
        title=AppSettings.APP_NAME,
        description=AppSettings.APP_DESCRIPTION,
        contact=AppSettings.APP_CONTACT
    )
    application.include_router(planning_router)

    return application


app = create_app()


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        "app.infra.http.fastapi:app", host=AppSettings.APP_HOST, port=AppSettings.APP_PORT, reload=True
    )
