from datetime import datetime

from app.core.entity.base import BaseEntity
from app.core.entity.patient import Patient


class PhysicalPlanning(BaseEntity):
    def __init__(
            self,
            patient: Patient,
            id_phase: int,
            anatomic_location: str,
            intent: str,
            modality: str,
            technique: str,
            daily_dose_tx: int,
            total_dose_tx: int,
            fractions: int,
            create_dt: datetime,
            edit_dt: datetime,
            **kwargs):
        super().__init__(**kwargs)
        self.patient = patient
        self.id_phase = id_phase
        self.anatomic_location = anatomic_location
        self.intent = intent
        self.modality = modality
        self.technique = technique
        self.daily_dose_tx = daily_dose_tx
        self.total_dose_tx = total_dose_tx
        self.fractions = fractions
        self.create_dt = create_dt
        self.edit_dt = edit_dt
