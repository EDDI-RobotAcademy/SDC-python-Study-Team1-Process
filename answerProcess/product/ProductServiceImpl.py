from product.ProductService import ProductService
from product.repository.ProductRepositoryImpl import ProductRepositoryImpl
from product.service.request.ProductRegisterRequest import ProductRegisterRequest
from product.service.response.ProductRegisterResponse import ProductRegisterResponse


class ProductServiceImpl(ProductService):
    __instance = None

    def __new__(cls, repository):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.repository = repository
        return cls.__instance

    def __init__(self, repository):
        print("TaskManageServiceImpl 생성자 호출")
        self.__productRepository = ProductRepositoryImpl()

    @classmethod
    def getInstance(cls, repository=None):
        if cls.__instance is None:
            cls.__instance = cls(repository)
        return cls.__instance

    def registerProduct(self, *args, **kwargs):
        cleanedElements = args[0]

        # for i, element in enumerate(cleanedElements):
        #     print(f"각각의 요소 {i + 1}: {element}")

        productRegisterRequest = ProductRegisterRequest(cleanedElements[0], cleanedElements[1])
        storedProduct = self.__productRepository.save(productRegisterRequest.toProduct())

        return ProductRegisterResponse(storedProduct.getId())

