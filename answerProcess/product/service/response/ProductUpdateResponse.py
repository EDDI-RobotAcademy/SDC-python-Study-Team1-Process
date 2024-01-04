from dataclasses import dataclass


@dataclass
class ProductUpdateResponse:
    __productNumber: int
    __productTitle: str
    __productDetails: str
    __seller: str
    __productPrice: int