from apps.blog.utils.api import BlogAbstractApiView as AbstractApiView
from apps.articles.models import Articles
from apps.articles.serializers.Articles import ArticlesSerializer
from django.http import JsonResponse
from django.template import loader
from django.forms.models import model_to_dict
from utils.paginator import ManagePagePagination
import datetime

class TimelineApi(AbstractApiView):
    def get_solution(self, requests):
        code = 200
        message = "Success"

        paginator = ManagePagePagination()
        exists = Articles.objects.filter(is_deleted=False).order_by("-update_time")
        recent = [model_to_dict(exists[i]) for i in range(len(exists))][:15]
        for i in range(len(recent)):
            recent[i]['coverImage'] = recent[i]['coverImage'].url.replace("/resources", "")
            recent[i]['create_time'] = exists[i].create_time
            recent[i]['create_time_formatted'] = exists[i].create_time.strftime("%Y-%m-%d")

        exists, num_pages = paginator.paginate_queryset(exists, requests, view=self)

        data = [model_to_dict(exists[i]) for i in range(len(exists))]
        for i in range(len(data)):
            data[i]['coverImage'] = data[i]['coverImage'].url.replace("/resources", "")
            data[i]['create_time'] = exists[i].create_time
            data[i]['create_time_formatted'] = exists[i].create_time.strftime("%Y-%m-%d")


        return {
            "code": code,
            "message": message,
            "data": {
                "data": data,
                "recent": recent
            },
            "template": loader.get_template("blog/timeline.html")
        }

    def post_solution(self, requests):
        code = 200
        message = "Success"

        paginator = ManagePagePagination()
        exists = Articles.objects.filter(is_deleted=False).order_by("-update_time")
        exists, num_pages = paginator.paginate_queryset(exists, requests, view=self)


        return {
            "code": code,
            "message": message,
            "data": model_to_dict(exists),
            "template": loader.get_template("blog/aboutMe.html")
        }