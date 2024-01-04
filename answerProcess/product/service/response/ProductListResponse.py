from dataclasses import dataclass

from product.entity.Product import Product


@dataclass
class ProductListResponse:
    __productNumber: int
    __productTitle: str
    __productPrice: int

