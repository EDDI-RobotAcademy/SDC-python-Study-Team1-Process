from dataclasses import dataclass


@dataclass
class ProductReadResponse:
    __productName: str
    __description: str
    __seller: str
    __price: str