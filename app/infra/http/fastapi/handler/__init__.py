from fastapi import Depends

from app.core.controller.planning_controller import PlanningController
from app.core.repository.planning_repository import PlanningRepository
from app.infra.database.database import Database


def get_database_instance():
    return Database()


def get_planning_repository(database: Database = Depends(get_database_instance)):
    return PlanningRepository(database)


def get_planning_controller(repository: PlanningRepository = Depends(get_planning_repository)):
    return PlanningController(repository)
