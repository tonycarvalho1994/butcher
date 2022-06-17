from datetime import timedelta

from app.core.entity.base import BaseEntity
from app.core.interfaces.repository_abc import RepositoryABC


class ShouldSyncUseCase:
    def __init__(self, repository: RepositoryABC, datetime_range: timedelta) -> None:
        self.repository = repository
        self.datetime_range = datetime_range

    def retrieve_updated_data_if_exists(self) -> list[BaseEntity] | bool:
        updated_data = self.repository.get_updated_data(self.datetime_range)

        return updated_data or False

    def retrieve_created_data_if_exists(self) -> list[BaseEntity] | bool:
        created_data = self.repository.get_created_data(self.datetime_range)

        return created_data or False
