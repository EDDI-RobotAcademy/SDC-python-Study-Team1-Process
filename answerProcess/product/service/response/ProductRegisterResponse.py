from dataclasses import dataclass


@dataclass
class ProductRegisterResponse:
    __productName: str
    __discription: str
    __seller: str