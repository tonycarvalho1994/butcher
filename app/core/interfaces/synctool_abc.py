from abc import ABC, abstractmethod

from app.core.entity.base import BaseEntity


class SyncToolABC(ABC):
    @abstractmethod
    def create_data(self, new_data: list[BaseEntity]) -> None: ...

    @abstractmethod
    def update_data(self, new_data: list[BaseEntity]) -> None: ...
