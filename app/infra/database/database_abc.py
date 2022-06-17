from abc import ABC, abstractmethod
from datetime import timedelta

from app.core.entity.base import BaseEntity
from app.core.repository import ModelType


class DatabaseABC(ABC):
    @abstractmethod
    def get_all(self, model: ModelType): ...

    @abstractmethod
    def get_updated_data(self, datetime_range: timedelta) -> list[BaseEntity] | None: ...

    @abstractmethod
    def get_created_data(self, datetime_range: timedelta) -> list[BaseEntity] | None: ...

    @abstractmethod
    def get_single_data(self, model: ModelType, object_id: str): ...

    @abstractmethod
    def create_data(self, model: ModelType, new_data: list[BaseEntity]): ...

    @abstractmethod
    def update_data(self, model: ModelType, new_data: list[BaseEntity]): ...
