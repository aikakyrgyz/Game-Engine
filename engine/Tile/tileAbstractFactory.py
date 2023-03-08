from abc import ABC, abstractmethod

from Sprite import sprite
from Tile import tileFactory


class TileAbstractFactory:
    def __init__(self):
        self._concreteFactories = {}

    def register_factory(self, key, factory):
        self._concreteFactories[key] = factory

    def create_tile(self, key):
        factory = self._concreteFactories.get(key)
        if not factory: # there is no factory with such a name
            raise ValueError(key)

        return factory() # since the factory defines __call__ function

    def get_factory_type(self, key):
        return type(self._concreteFactories.get(key))



# https://realpython.com/factory-method-python/


