from app.core.entity.physical_planning import PhysicalPlanning
from app.core.repository.planning_repository import PlanningRepository


class PlanningController:
    def __init__(self, repository: PlanningRepository):
        self.repository = repository

    def get_planning_by_id_patient(self, id_patient: str) -> PhysicalPlanning | None:
        return self.repository.get_data_by_id_patient(id_patient)

    def get_planning_by_id_sisac(self, id_sisac: str) -> PhysicalPlanning | None:
        return self.repository.get_data_by_id_sisac(id_sisac)

    def get_planning_by_id_mosaiq(self, id_mosaiq: str) -> PhysicalPlanning | None:
        return self.repository.get_data_by_id_mosaiq(id_mosaiq)

    def get_all_plannings(self) -> list[PhysicalPlanning] | None:
        return self.repository.get_all_data()
