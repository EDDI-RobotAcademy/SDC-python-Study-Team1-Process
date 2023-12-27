from dataclasses import dataclass


@dataclass
class ProductRegisterResponse:
    __productName: str
    __description: str
    __seller: str
    __price: str