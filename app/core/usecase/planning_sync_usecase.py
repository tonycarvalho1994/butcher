from app.core.entity.physical_planning import PhysicalPlanning
from app.core.interfaces.synctool_abc import SyncToolABC
from app.core.repository.planning_repository import PlanningRepository


class PlanningSyncUseCase(SyncToolABC):
    def __init__(self, repository: PlanningRepository):
        self.repository = repository

    def create_data(self, new_data: list[PhysicalPlanning]):
        self.repository.create_data(new_data)

    def update_data(self, new_data: list[PhysicalPlanning]):
        self.repository.update_data(new_data)
