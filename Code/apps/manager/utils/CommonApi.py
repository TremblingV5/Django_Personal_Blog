from apps.manager.utils.api import AbstractApiView
from django.forms.models import model_to_dict


class CommonApi(AbstractApiView):

    CODE = 200
    TARGET = None

    def get_solution(self, requests):
        exists = self.TARGET.objects.filter(is_deleted=False)
        return {
            "data": [model_to_dict(exists[i]) for i in range(len(exists))]
        }
