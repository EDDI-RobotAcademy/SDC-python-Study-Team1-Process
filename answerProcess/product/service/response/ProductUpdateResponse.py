from dataclasses import dataclass


@dataclass
class ProductUpdateResponse:
    __productNumber: int
    __productName: str
    __description: str
    __seller: str
    __price: float