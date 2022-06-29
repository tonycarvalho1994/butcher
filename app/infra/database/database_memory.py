from app.core.repository import ObjectReferences
from app.infra.database.database_abc import DatabaseABC
from app.infra.database.fixture import MEMORY_DATABASE


class DatabaseMemory(DatabaseABC):
    db = MEMORY_DATABASE.copy()

    def get_data(self, model: str, object_id: str, object_reference: str):
        query_params = {}

        match object_reference:
            case ObjectReferences.PATIENT:
                query_params.update({'id_patient': object_id})
            case ObjectReferences.PLANNING:
                query_params.update({'id_planning': object_id})
            case _:
                raise Exception('Invalid object reference. Must be one of ObjectReferences Class')

        result = self.db.get(model.value)

        return [row for row in result]
