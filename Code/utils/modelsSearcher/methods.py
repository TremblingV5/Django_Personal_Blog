from utils.modelsSearcher.ModelsSearcherConfig import ModelsSearcherConfig as cfg
from utils.modelsSearcher.abstractMethods import ModelsSearcher

class ManagerSearcherMethod(ModelsSearcher):

    def search(self, target, **args):
        print(target, args)
        exists = cfg[target]['model'].objects.filter(**args)
        print(exists)
