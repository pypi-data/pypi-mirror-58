from dataclasses import asdict
from typing import Any, ClassVar, Dict


class Resource:
    _client: ClassVar['stpmex.Client']  # type: ignore
    _endpoint: ClassVar[str]
    empresa: ClassVar[str]

    @property
    def firma(self):
        ...  # pragma: no cover

    def to_dict(self) -> Dict[str, Any]:
        base = {k: v for k, v in asdict(self).items() if v}
        return {**base, **dict(firma=self.firma, empresa=self.empresa)}
