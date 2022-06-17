from datetime import date
from typing import Optional

from app.core.entity.base import BaseEntity


class Patient(BaseEntity):
    def __init__(self,
                 first_name: str,
                 last_name: str,
                 cpf: str,
                 birth_date: date,
                 id_mosaiq: Optional[str | None] = None,
                 id_sisac: Optional[str | None] = None,
                 **kwargs) -> None:
        super().__init__(**kwargs)
        self.id_sisac = id_sisac
        self.id_mosaiq = id_mosaiq
        self.first_name = first_name
        self.last_name = last_name
        self.cpf = cpf
        self.birth_date = birth_date

    @property
    def full_name(self):
        return f'{self.first_name} {self.first_name}'
