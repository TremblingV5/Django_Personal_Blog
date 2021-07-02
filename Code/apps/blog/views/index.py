from apps.blog.utils.api import BlogAbstractApiView as AbstractApiView
from django.http import JsonResponse
from django.template import loader
from django.forms.models import model_to_dict


class IndexApi(AbstractApiView):

    CODE = 200
    TEMPLATE = "blog/index.html"

    def get_solution(self, requests):
        return {
            "data": []
        }
