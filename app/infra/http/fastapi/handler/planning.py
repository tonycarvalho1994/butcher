from fastapi import APIRouter, Depends

from app.core.controller.planning_controller import PlanningController
from app.core.repository import ObjectReferences
from app.core.schemas.planning import PhysicalPlanningSchema
from app.infra.http.fastapi.handler import get_planning_controller

planning_router = APIRouter(
    prefix='/planning',
    tags=['Planning']
)


@planning_router.get(
    path='/id_patient/{id_patient}',
    description='Endpoint that shows physical planning stored on database.',
    response_model=list[PhysicalPlanningSchema]
)
def get_plannings_by_id_patient(
        id_patient: str,
        controller: PlanningController = Depends(get_planning_controller)):
    return controller.get_planning(
        object_id=id_patient,
        object_reference=ObjectReferences.PATIENT
    )


@planning_router.get(
    path='/id_planning/{id_planning}',
    description='Endpoint that shows physical planning stored on database.',
    response_model=list[PhysicalPlanningSchema]
)
def get_plannings_by_id_planning(
        id_planning: str,
        controller: PlanningController = Depends(get_planning_controller)):
    return controller.get_planning(
        object_id=id_planning,
        object_reference=ObjectReferences.PLANNING
    )
