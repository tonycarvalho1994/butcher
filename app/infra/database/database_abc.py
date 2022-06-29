from abc import ABC, abstractmethod


class DatabaseABC(ABC):
    @abstractmethod
    def get_data(self, model: str, object_id: str, object_reference: str): ...
