from fastapi import FastAPI

from app.settings import AppSettings
from app.infra.http.fastapi.handler.planning import planning_router

app = FastAPI(
    title=AppSettings.APP_NAME,
    description=AppSettings.APP_DESCRIPTION,
    contact=AppSettings.APP_CONTACT
)

app.include_router(planning_router)
