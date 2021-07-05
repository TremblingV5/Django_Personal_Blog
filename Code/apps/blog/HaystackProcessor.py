from haystack.signals import RealtimeSignalProcessor
from haystack.exceptions import NotHandled
from django.db import models

class Processor(RealtimeSignalProcessor):

    def setup(self):
        models.signals.post_save.connect(self.handle_save)
        models.signals.post_delete.connect(self.handle_delete)

    def handle_save(self, sender, instance, **kwargs):
        using_backends = self.connection_router.for_write(instance=instance)

        for using in using_backends:
            try:
                index = self.connections[using].get_unified_index().get_index(sender)
                index.update_object(instance, using=using)
            except NotHandled:
                raise Exception("NotHandled")