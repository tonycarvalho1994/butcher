from typing import Optional

from pydantic import BaseModel


class BaseEntity(BaseModel):
    id_sisac: Optional[str | None]
    id_mosaiq: Optional[str | None]
