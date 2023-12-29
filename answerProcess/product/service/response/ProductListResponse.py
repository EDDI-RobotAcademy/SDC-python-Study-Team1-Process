from dataclasses import dataclass

from product.entity.Product import Product


@dataclass
class ProductListResponse:
    __productNumber: int
    __productName: str
    __description: str
    __seller: str
    __price: float

