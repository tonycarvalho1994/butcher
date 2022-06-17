from abc import ABC, abstractmethod
from datetime import timedelta

from app.core.entity.base import BaseEntity


class RepositoryABC(ABC):
    @abstractmethod
    def get_updated_data(self, datetime_range: timedelta) -> list[BaseEntity] | None: ...

    @abstractmethod
    def get_created_data(self, datetime_range: timedelta) -> list[BaseEntity] | None: ...

    @abstractmethod
    def create_data(self, new_data: list[BaseEntity]): ...

    @abstractmethod
    def update_data(self, new_data: list[BaseEntity]): ...

    @abstractmethod
    def get_data_by_id_patient(self, id_patient: str) -> BaseEntity | None: ...

    @abstractmethod
    def get_data_by_id_sisac(self, id_sisac: str) -> BaseEntity | None: ...

    @abstractmethod
    def get_data_by_id_mosaiq(self, id_mosaiq: str) -> BaseEntity | None: ...

    @abstractmethod
    def get_all_data(self) -> list[BaseEntity] | None: ...
