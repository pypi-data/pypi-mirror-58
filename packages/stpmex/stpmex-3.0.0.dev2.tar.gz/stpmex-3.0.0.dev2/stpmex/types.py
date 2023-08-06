from enum import Enum
from typing import Optional, Type

from pydantic import constr


def truncated_str(length) -> Type:
    return constr(strip_whitespace=True, min_length=1, curtail_length=length)


def digits(
    min_length: Optional[int] = None, max_length: Optional[int] = None
) -> Type:
    return constr(regex=r'^\d+$', min_length=min_length, max_length=max_length)


class Prioridad(Enum):
    normal = 0
    alta = 1


class TipoCuenta(Enum):
    card = 3
    phone_number = 10
    clabe = 40
