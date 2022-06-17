from datetime import timedelta

from app.core.entity.base import BaseEntity
from app.core.repository import ModelType
from app.infra.database.database_abc import DatabaseABC


class Database(DatabaseABC):
    def get_all(self, model: ModelType):
        return {
            model: 'Listing all rows for the given model. Heheheheh'
        }

    def get_updated_data(self, datetime_range: timedelta) -> list[BaseEntity] | None:
        pass

    def get_created_data(self, datetime_range: timedelta) -> list[BaseEntity] | None:
        pass

    def get_single_data(self, model: ModelType, object_id: str):
        pass

    def create_data(self, model: ModelType, new_data: list[BaseEntity]):
        pass

    def update_data(self, model: ModelType, new_data: list[BaseEntity]):
        pass
