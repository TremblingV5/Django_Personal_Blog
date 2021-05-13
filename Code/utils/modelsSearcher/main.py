from utils.modelsSearcher.interface import ModelsSearcherHandler
from utils.modelsSearcher.methods import ManagerSearcherMethod


def manage_get(target, **args):
    handle = ModelsSearcherHandler()
    handle.method = ManagerSearcherMethod()
    handle.search(target=target, **args)
