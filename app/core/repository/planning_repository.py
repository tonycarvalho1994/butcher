from app.core.interfaces.repository_abc import RepositoryABC
from app.core.repository import Repositories, ObjectReferences
from app.core.schemas.planning import PhysicalPlanningSchema
from app.core.schemas.txfield import TxFieldSchema
from app.infra.database.database_abc import DatabaseABC


class PlanningRepository(RepositoryABC):
    def __init__(self, database: DatabaseABC):
        self.database = database

    def get_data(
            self,
            model: str,
            object_id: str | int,
            object_reference: str
    ) -> list[PhysicalPlanningSchema] | list[TxFieldSchema]:
        results = self.database.get_data(
            model=model,
            object_id=object_id,
            object_reference=object_reference
        )

        match model:
            case Repositories.PLANNING:
                return [PhysicalPlanningSchema(**row) for row in results]
            case Repositories.TX_FIELD:
                return [TxFieldSchema(**row) for row in results]
            case _:
                raise Exception('Invalid Model. Must be one of Repositories Class')
