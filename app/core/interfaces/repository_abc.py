from abc import ABC, abstractmethod

from app.core.entity.base import BaseEntity


class RepositoryABC(ABC):
    @abstractmethod
    def get_data(self, model: str, id_patient: str, object_reference: str) -> BaseEntity | None: ...
