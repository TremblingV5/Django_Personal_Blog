import importlib

class getter(object):

    def __init__(self, path, attr):
        self.module = getattr(importlib.import_module("apps.%s" % path), attr)

    def get(self):
        pass
