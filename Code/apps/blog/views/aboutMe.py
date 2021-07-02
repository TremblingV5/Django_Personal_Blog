from apps.blog.utils.api import BlogAbstractApiView as AbstractApiView
from utils.parser import parse_md
from apps.blog.models import AboutMe
from apps.articles.models import Articles
from django.http import JsonResponse
from django.template import loader
from django.forms.models import model_to_dict
from imagekit.models.fields.files import ProcessedImageFieldFile


class AboutMeApi(AbstractApiView):

    CODE = 200
    TEMPLATE = "blog/aboutMe.html"

    def get_solution(self, requests):

        exists = AboutMe.objects.filter()
        content = parse_md(model_to_dict(exists[0])['content'])

        exists = Articles.objects.filter(is_deleted=False).order_by("-update_time")
        recent = [model_to_dict(exists[i]) for i in range(len(exists))]

        for item in recent:
            for k in item:
                if isinstance(item[k], ProcessedImageFieldFile):
                    item[k] = item[k].name

        return {
            "data": {
                'content': content,
                'recent': recent[:10]
            }
        }

class GetAboutMeApi(AbstractApiView):

    CODE = 200
    TEMPLATE = "blog/articlePage.html"

    def get_solution(self, requests):

        exists = AboutMe.objects.filter()
        content = parse_md(model_to_dict(exists[0])['content'])

        return {
            "data": {
                'content': content
            }
        }
