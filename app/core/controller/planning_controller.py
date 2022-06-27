from app.core.repository import Repositories, ObjectReferences
from app.core.repository.planning_repository import PlanningRepository
from app.core.schemas.planning import PhysicalPlanningSchema


class PlanningController:
    def __init__(self, repository: PlanningRepository):
        self.repository = repository

    def get_planning(
            self,
            object_id: str,
            object_reference: str
    ) -> list[PhysicalPlanningSchema] | None:
        plannings = self.repository.get_data(
            model=Repositories.PLANNING,
            object_id=object_id,
            object_reference=object_reference
        )

        if not plannings:
            return None

        for planning in plannings:
            field_list = self.repository.get_data(
                model=Repositories.TX_FIELD,
                object_id=planning.id_phase,
                object_reference=ObjectReferences.PLANNING
            )
            planning.field_list = field_list

        return plannings
