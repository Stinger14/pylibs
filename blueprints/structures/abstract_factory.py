"The Factory Design Pattern concept"
from abc import ABCMeta, abstractmethod


class IProduct(metaclass=ABCMeta):
    "Class interface for (Product)"
    @staticmethod
    @classmethod
    def create_object(cls):
        "An abstract interface method"


class ConcreteProductA(IProduct):
    "A Concrete class that implements the IProduct interface"

    def __init__(self):
        self.name = "ConcreteProductA"

    def create_object(self):
        return self


class ConcreteProductB(IProduct):
    "A Concrete class that implements the IProduct interface"

    def __init__(self):
        self.name = "ConcreteProductB"

    def create_object(self):
        return self


class ProductFactory:
    "The Factory class"

    @staticmethod
    def create_object(prop):
        "A static method to get a concrete product"
        if prop == 'XML':
            return ConcreteProductA()
        if prop == 'JSON':
            return ConcreteProductB()
        if prop == 'LUA':
            return None

# Client
PRODUCT = ProductFactory().create_object('XML')
print(PRODUCT.name)

