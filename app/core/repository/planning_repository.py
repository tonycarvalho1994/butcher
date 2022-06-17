from datetime import timedelta

from app.core.entity.base import BaseEntity
from app.core.entity.physical_planning import PhysicalPlanning
from app.core.interfaces.repository_abc import RepositoryABC
from app.core.repository import Repositories
from app.infra.database.database_abc import DatabaseABC


class PlanningRepository(RepositoryABC):
    def __init__(self, database: DatabaseABC):
        self.database = database

    def get_updated_data(self, datetime_range: timedelta) -> list[PhysicalPlanning] | None:
        return self.database.get_updated_data(datetime_range)

    def get_created_data(self, datetime_range: timedelta) -> list[PhysicalPlanning] | None:
        return self.database.get_created_data(datetime_range)

    def create_data(self, new_data: list[PhysicalPlanning]):
        self.database.create_data(Repositories.PLANNING, new_data)

    def update_data(self, new_data: list[PhysicalPlanning]):
        self.database.update_data(Repositories.PLANNING, new_data)

    def get_data_by_id_patient(self, id_patient: str) -> BaseEntity | None:
        return {
            'planning': f'Listing planning fetched by id patient {id_patient}'
        }

    def get_data_by_id_sisac(self, id_sisac: str) -> PhysicalPlanning | None:
        return {
            'planning': 'Listing planning fetched by id sisac'
        }

    def get_data_by_id_mosaiq(self, id_mosaiq: str) -> PhysicalPlanning | None:
        return {
            'planning': 'Listing planning fetched by id mosaiq'
        }

    def get_all_data(self) -> list[PhysicalPlanning] | None:
        return self.database.get_all(Repositories.PLANNING)
