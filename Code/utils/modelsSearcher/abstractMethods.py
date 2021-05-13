from abc import ABC, abstractmethod

class ModelsSearcher(ABC):

    @abstractmethod
    def search(self):
        pass
