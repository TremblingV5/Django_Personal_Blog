from django.forms.models import model_to_dict

from apps.manager.utils.api import AbstractApiView


class CommonApi(AbstractApiView):

    CODE = 200
    TARGET = None

    def get_solution(self, requests):
        try:
            exists = self.TARGET.objects.filter(is_deleted=False)
        except:
            exists = self.TARGET.objects.all()
        return {
            "data": [model_to_dict(exists[i]) for i in range(len(exists))]
        }
