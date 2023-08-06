from typing import Any, ClassVar, Dict

from OpenSSL import crypto
from requests import Response, Session

from .exc import InvalidPassphrase, StpmexException
from .resources import Orden, Resource
from .version import __version__ as client_version

DEMO_BASE_URL = 'https://demo.stpmex.com:7024/speidemows/rest'
PROD_BASE_URL = 'https://prod.stpmex.com/speiws/rest'


class Client:

    base_url: str
    demo: bool
    headers: Dict[str, str]
    session: Session

    # resources
    ordenes: ClassVar = Orden

    def __init__(
        self,
        empresa: str,
        priv_key: str,
        priv_key_passphrase: str,
        demo: bool = False,
    ):
        self.session = Session()
        self.headers = {'User-Agent': f'stpmex-python/{client_version}'}
        if demo:
            self.base_url = DEMO_BASE_URL
        else:
            self.base_url = PROD_BASE_URL
        try:
            self.pkey = crypto.load_privatekey(
                crypto.FILETYPE_PEM,
                priv_key,
                priv_key_passphrase.encode('ascii'),
            )
        except crypto.Error:
            raise InvalidPassphrase
        Resource.empresa = empresa
        Resource._client = self

    def put(
        self, endpoint: str, data: Dict[str, Any], **kwargs: Any
    ) -> Dict[str, Any]:
        return self.request('put', endpoint, data, **kwargs)

    def request(
        self, method: str, endpoint: str, data: Dict[str, Any], **kwargs: Any
    ) -> Dict[str, Any]:
        url = self.base_url + endpoint
        response = self.session.request(
            method, url, json=data, headers=self.headers, **kwargs
        )
        self._check_response(response)
        return response.json()['resultado']

    @staticmethod
    def _check_response(response: Response) -> None:
        if response.ok:
            resultado = response.json()['resultado']
            if 'descripcionError' in resultado:
                raise StpmexException(**resultado)
        response.raise_for_status()
