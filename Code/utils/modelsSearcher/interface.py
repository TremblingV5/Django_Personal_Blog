# -*- coding: utf-8 -*-
from abc import ABC
from utils.modelsSearcher.abstractMethods import ModelsSearcher


class ModelsSearcherHandler(ABC):

    def __init__(self, method=None):
        self._method = method

    @property
    def method(self) -> ModelsSearcher:
        return self._method

    @method.setter
    def method(self, method: ModelsSearcher):
        self._method = method

    def search(self, **args):
        return self._method.search(**args)
