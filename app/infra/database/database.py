from app.infra.database import get_db
from app.infra.database.database_abc import DatabaseABC
from app.core.repository import ObjectReferences, Repositories
from app.infra.database.query import query_get_plannings, query_get_txfields


class Database(DatabaseABC):
    def get_data(self, model: str, object_id: str, object_reference: str):
        query_params = {}
        query = ''

        match object_reference:
            case ObjectReferences.PATIENT:
                query_params.update({'id_patient': object_id})
            case ObjectReferences.PLANNING:
                query_params.update({'id_planning': object_id})
            case _:
                raise Exception('Invalid object reference. Must be one of ObjectReferences Class')

        match model:
            case Repositories.PLANNING:
                query = query_get_plannings(query_params)
            case Repositories.TX_FIELD:
                query = query_get_txfields(query_params)
            case _:
                raise Exception('Invalid Model. Must be one of Repositories Class')

        db = get_db()
        result = db.execute(query)

        return [row for row in result]
