from enum import Enum


class Repositories(Enum):
    PLANNING: str = 'planning'
    TX_FIELD: str = 'tx_field'


class ObjectReferences(Enum):
    PATIENT: str = 'patient'
    PLANNING: str = 'planning'
