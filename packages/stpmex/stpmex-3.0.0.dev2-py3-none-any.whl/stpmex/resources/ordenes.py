import random
import time
import unicodedata
from dataclasses import field
from typing import ClassVar, Optional

import clabe
from pydantic import PositiveFloat, conint, constr, validator
from pydantic.dataclasses import dataclass

from ..auth import ORDEN_FIELDNAMES, compute_signature, join_fields
from ..types import Prioridad, TipoCuenta, digits, truncated_str
from .base import Resource

STP_BANK_CODE = '90646'


@dataclass
class Orden(Resource):
    """
    Base on:
    https://stpmex.zendesk.com/hc/es/articles/360002682851-RegistraOrden-Dispersi%C3%B3n-
    """

    _endpoint: ClassVar[str] = '/ordenPago'

    monto: PositiveFloat
    conceptoPago: truncated_str(39)

    nombreBeneficiario: truncated_str(39)
    cuentaBeneficiario: digits(10, 19)
    institucionContraparte: digits(5, 5)
    tipoCuentaBeneficiario: int

    nombreOrdenante: Optional[truncated_str(39)] = None
    cuentaOrdenante: Optional[digits(10, 19)] = None
    institucionOperante: digits(5, 5) = STP_BANK_CODE
    tipoCuentaOrdenante: Optional[int] = None

    claveRastreo: truncated_str(29) = field(
        default_factory=lambda: f'CR{int(time.time())}'
    )
    referenciaNumerica: conint(gt=0, lt=10 ** 7) = field(
        default_factory=lambda: random.randint(10 ** 6, 10 ** 7)
    )
    rfcCurpBeneficiario: constr(max_length=18) = 'ND'
    rfcCurpOrdenante: Optional[constr(max_length=18)] = None
    medioEntrega: int = 3
    prioridad: int = Prioridad.alta.value
    tipoPago: int = 1
    topologia: str = 'T'
    iva: Optional[float] = None

    id: Optional[int] = None

    @classmethod
    def create(cls, **kwargs):
        orden = cls(**kwargs)
        endpoint = orden._endpoint + '/registra'
        resp = orden._client.put(endpoint, orden.to_dict())
        orden.id = resp['id']
        return orden

    @property
    def firma(self):
        """
        Based on:
        https://stpmex.zendesk.com/hc/es/articles/360002796012-Firmas-Electr%C3%B3nicas-
        """
        joined_fields = join_fields(self, ORDEN_FIELDNAMES)
        return compute_signature(self._client.pkey, joined_fields)

    def __post_init__(self):
        # Test before Pydantic coerces it to a float
        if not isinstance(self.monto, float):
            raise ValueError('monto must be a float')

    @validator('cuentaBeneficiario', 'cuentaOrdenante', each_item=True)
    def _validate_cuenta(cls, v):
        if len(v) == 18:
            if not clabe.validate_clabe(v):
                raise ValueError('cuenta no es una válida CLABE')
        elif not len(v) in {10, 15, 16}:
            raise ValueError('cuenta no es válida')
        return v

    @validator('institucionContraparte', 'institucionOperante', each_item=True)
    def _validate_institucion(cls, v):
        if v not in clabe.BANKS.values():
            raise ValueError(f'{v} no se corresponde a un banco')
        return v

    @staticmethod
    def _validate_tipoCuenta(fieldname, tipo, values):
        try:
            cuenta = values[fieldname]
        except KeyError:  # there's a validation error elsewhere
            return tipo
        if not any(
            [
                len(cuenta) == 10 and tipo == TipoCuenta.phone_number.value,
                len(cuenta) in {15, 16} and tipo == TipoCuenta.card.value,
                len(cuenta) == 18 and tipo == TipoCuenta.clabe.value,
            ]
        ):
            raise ValueError('tipoCuenta no es válido')
        return tipo

    @validator('tipoCuentaBeneficiario')
    def _validate_tipoCuentaBeneficiario(cls, v, values):
        return cls._validate_tipoCuenta('cuentaBeneficiario', v, values)

    @validator('tipoCuentaOrdenante', each_item=True)
    def _validate_tipoCuentaOrdenante(cls, v, values):
        return cls._validate_tipoCuenta('cuentaOrdenante', v, values)

    @validator(
        'nombreBeneficiario', 'nombreOrdenante', 'conceptoPago', each_item=True
    )
    def _unicode_to_ascii(cls, v):
        v = unicodedata.normalize('NFKD', v).encode('ascii', 'ignore')
        return v.decode('ascii')
