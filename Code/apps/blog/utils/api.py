from django.conf import settings
from django.forms.models import model_to_dict

from apps.articles.models import Articles
from apps.resume.models import BasicInfo
from utils.api import AbstractApiView


class BlogAbstractApiView(AbstractApiView):

    def data_wrap(self, responseData):
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

        responseData.update({
            "slider": self.replace_not_json(slider),
            "recentA": self.replace_not_json(recentArticles[0]),
            "recentB": self.replace_not_json(recentArticles[1]),
            "intro": self_introduction,
            "recent_footer": self.replace_not_json(recent_footer[:5]),
            "basic": {
                "phone": basic.mobile,
                "email": basic.email,
                "website": basic.website
            },
            "config": settings.SITE_CONFIG
        })

        return responseData

    def put(self, requests):
        pass

    def delete(self, requests):
        pass

    def post_solution(self, requests):
        pass

    def get_solution(self, requests):
        pass

    def replace_not_json(self, data):
        if self.reqType == "json":
            for item in data:
                if "coverImage" in item:
                    item["coverImage"] = item['coverImage'].url.replace("/resources", "")
        return data