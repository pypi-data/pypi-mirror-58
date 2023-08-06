# STP python3.6+ client library

[![Build Status](https://travis-ci.com/cuenca-mx/stpmex-python.svg?branch=master)](https://travis-ci.com/cuenca-mx/stpmex-python)
[![Coverage Status](https://coveralls.io/repos/github/cuenca-mx/stpmex-python/badge.svg?branch=master)](https://coveralls.io/github/cuenca-mx/stpmex-python?branch=master)
[![PyPI](https://img.shields.io/pypi/v/stpmex.svg)](https://pypi.org/project/stpmex/)

Cliente para el servicio SOAP de STP


## Requerimientos

Python v3.6 o superior.

## Documentación de API

[General](https://stpmex.zendesk.com/hc/es) y
[WADL](https://demo.stpmex.com:7024/speidemows/rest/application.wadl?metadata=true&detail=true)

## Instalación

```
pip install stpmex
```

## Correr pruebas

```
make venv
source venv/bin/activate
make test
```

## Uso básico

```python
from stpmex import Client

client = Client(
    empresa='TU_EMPRESA',
    priv_key='PKEY_CONTENIDO',
    priv_key_passphrase='supersecret'
)
orden = client.ordenes.create(
    institucionContraparte='40072',
    monto=1.2,
    nombreBeneficiario='Ricardo Sanchez',
    tipoCuentaBeneficiario=40,
    cuentaBeneficiario='072691004495711499',
    conceptoPago='Prueba',
)
```
