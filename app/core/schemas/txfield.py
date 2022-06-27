from datetime import datetime

from pydantic import BaseModel


class TxFieldSchema(BaseModel):
    id_field: int
    id_patient: str
    id_planning: int
    name: str
    number: int
    dose: int
    meter_set: int
    energy: int
    energy_unit_enum: int
    gantry_ang: int
    collimator_ang: int
    couch_ang: int
    create_dt: datetime
    edit_dt: datetime
