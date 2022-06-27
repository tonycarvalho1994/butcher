from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from app.core.schemas.txfield import TxFieldSchema


class PhysicalPlanningSchema(BaseModel):
    id_phase: int
    id_patient: str
    anatomic_location: str
    intent: str
    modality: str
    technique: str
    daily_dose_tx: int
    total_dose_tx: int
    fractions: int
    create_dt: datetime
    edit_dt: datetime
    field_list: Optional[list[TxFieldSchema]] = None
