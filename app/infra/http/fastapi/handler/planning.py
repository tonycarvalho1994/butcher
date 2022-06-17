from fastapi import APIRouter, Depends

from app.core.controller.planning_controller import PlanningController
from app.infra.http.fastapi.handler import get_planning_controller

planning_router = APIRouter(
    prefix='/planning',
    tags=['Planning']
)


@planning_router.get(
    path='/',
    description='Endpoint that shows physical planning stored on database.'
)
def get_plannings(
        id_patient: str | None = None,
        id_sisac: str | None = None,
        id_mosaiq: str | None = None,
        controller: PlanningController = Depends(get_planning_controller)):
    if id_patient:
        return controller.get_planning_by_id_patient(id_patient)

    if id_sisac:
        return controller.get_planning_by_id_sisac(id_sisac)

    if id_mosaiq:
        return controller.get_planning_by_id_mosaiq(id_mosaiq)

    return controller.get_all_plannings()

