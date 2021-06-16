from utils.api import AbstractApiView
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.forms.models import model_to_dict

from apps.resume.models import BasicInfo
from apps.articles.models import Articles
from apps.articles.serializers.Articles import ArticlesSerializer

class BlogAbstractApiView(AbstractApiView):
    """
    不要重写 post, get两个方法
    """
    def post(self, requests):
        result = self.post_solution(requests)
        type = requests.POST.get("type")
        if type == "json":
            return JsonResponse({
                "code": result["code"],
                "message": result["message"],
                "data": result["data"]
            })
        else:
            return HttpResponse(
                result["template"].render({
                    "code": result["code"],
                    "message": result["message"],
                    "data": result["data"],
                    "config": settings.SITE_CONFIG
                }, requests)
            )

    def get(self, requests):
        result = self.get_solution(requests)
        type = requests.GET.get("type")

        try:
            exists = Articles.objects.filter(is_deleted=False, in_turn=True).order_by("id")
            slider = [model_to_dict(exists[i]) for i in range(len(exists))]
            for i in range(len(exists)):
                slider[i]['cate_id'] = exists[i].cate_id.name
        except:
            slider = []

        recentArticles = [[], []]
        try:
            exists = Articles.objects.filter(is_deleted=False).order_by("-update_time")
            recent = [model_to_dict(exists[i]) for i in range(len(exists))]
            if len(recent) > 3 and len(recent) < 6:
                recentArticles = [recent[:3], []]
            elif len(recent) > 6:
                recentArticles = [recent[:3], recent[4: 7]]
            else:
                recentArticles = [[], []]
        except:
            recentArticles = [[], []]

        try:
            exists = BasicInfo.objects.filter(is_deleted=False)
            basic = exists[0]
            self_introduction = exists[0].introduction
        except:
            self_introduction = []
            basic = BasicInfo()

        try:
            exists = Articles.objects.filter(is_deleted=False).order_by("-update_time")
            recent_footer = [model_to_dict(exists[i]) for i in range(len(exists))]
        except:
            recent_footer = []

        if type == "json":
            return JsonResponse({
                "code": result["code"],
                "message": result["message"],
                "data": result["data"]
            })
        else:
            return HttpResponse(
                result["template"].render({
                    "code": result["code"],
                    "message": result["message"],
                    "slider": slider,
                    "recentA": recentArticles[0],
                    "recentB": recentArticles[1],
                    "data": result["data"],
                    "intro": self_introduction,
                    "recent_footer": recent_footer[:5],
                    "basic": {
                        "phone": basic.mobile,
                        "email": basic.email,
                        "website": basic.website
                    },
                    "config": settings.SITE_CONFIG
                }, requests)
            )

    def put(self, requests):
        pass

    def delete(self, requests):
        pass

    def post_solution(self, requests):
        """
        :param requests:
        :return:
            一个字典对象，包含如下索引：code、message、data、http_code、templates
            需要将http返回的报文的状态码设置为http_code
        """
        pass

    def get_solution(self, requests):
        pass
