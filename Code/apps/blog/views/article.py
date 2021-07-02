from apps.blog.utils.api import BlogAbstractApiView as AbstractApiView
from utils.parser import parse_md
from apps.articles.models import Articles
from apps.resume.models import BasicInfo
from django.http import HttpResponseRedirect
from django.http import HttpResponse, JsonResponse
from apps.articles.serializers.Articles import ArticlesSerializer
from django.http import JsonResponse
from django.template import loader
from django.forms.models import model_to_dict
import markdown

class ArticleApi(AbstractApiView):

    CODE = 200

    def get(self, requests, article_id):
        code = 200
        message = "Success"

        t = requests.GET.get("type")
        if article_id == None:
            return HttpResponseRedirect('/blog/index/')

        exists = Articles.objects.filter(id=article_id, is_deleted=False)

        data = model_to_dict(exists[0])

        data['content'] = parse_md(data['content'])

        if not len(exists) > 0:
            return HttpResponseRedirect('/blog/index/')

        try:
            exists = BasicInfo.objects.filter(is_deleted=False)
            basic = exists[0]
            intro = exists[0].introduction
        except:
            intro = ""

        try:
            exists = Articles.objects.filter(is_deleted=False).order_by("-update_time")
            recent_footer = [model_to_dict(exists[i]) for i in range(len(exists))]
        except:
            recent_footer = []

        result = {
            "code": code,
            "message": message,
            "data": data,
            "intro": intro,
            "recent_footer": recent_footer[:5],
            "basic": {
                "phone": basic.mobile,
                "email": basic.email,
                "website": basic.website
            }
        }

        if t == "json":
            return JsonResponse(result)
        else:
            return HttpResponse(
                loader.get_template("blog/article.html").render(result, requests)
            )
