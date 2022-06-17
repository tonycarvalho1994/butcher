from enum import Enum
from typing import Literal


class Repositories(Enum):
    PLANNING: str = 'planning'
    TX_FIELD: str = 'tx_field'


ModelType = Literal[Repositories.PLANNING, Repositories.TX_FIELD]
