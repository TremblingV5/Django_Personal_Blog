from apps.manager.utils.api import ManageAbstractApiView as AbstractApiView
from django.http import JsonResponse
from django.template import loader
from django.forms.models import model_to_dict
from apps.articles.models import ArticleCategories
from apps.articles.serializers.ArticleCategories import ArticleCategoriesSerializer

class ArticleCategoryApi(AbstractApiView):
    def get_solution(self, requests):
        code = 200
        message = "Success"

        exists = ArticleCategories.objects.filter(is_deleted=False)
        return {
            "code": code,
            "message": message,
            "data": [model_to_dict(exists[i]) for i in range(len(exists))],
            "template": loader.get_template("manage/articleCategory.html")
        }

    def post_solution(self, requests):
        code = 200
        message = "Success"


        return {
            "code": code,
            "message": message,
            "data": {},
            "template": loader.get_template("manage/modifyArticleCategory.html")
        }

class ModifyArticleCategoryApi(AbstractApiView):
    def get_solution(self, requests):
        code = 200
        message = "Success"
        data = {}

        record_id = requests.GET.get('id')

        if record_id != None:
            exists = ArticleCategories.objects.filter(id=record_id)
            if len(exists) == 1:
                data = exists[0]

        return {
            "code": code,
            "message": message,
            "data": data,
            "template": loader.get_template("manage/modifyArticleCategory.html")
        }

    def post_solution(self, requests):
        code = 200
        message = "Success"

        res = ArticleCategoriesSerializer(data=requests.data, many=False)
        if res.is_valid(raise_exception=True):
            if requests.POST.get('id') != "":
                exists = ArticleCategories.objects.filter(id=requests.POST.get('id'))
                res.update(exists[0], res.data)
            else:
                res.create(res.data)

        return {
            "code": code,
            "message": message,
            "data": {},
            "template": loader.get_template("manage/200.html")
        }

    def delete(self, requests):
        code = 0
        message = "None"

        id = requests.POST.get('id')
        exists = ArticleCategories.objects.filter(id=id)
        if len(exists) > 0:
            exists[0].is_deleted = True
            exists[0].save()
            code = 200
            message = "delete success"

        return JsonResponse({
            "code": code,
            "message": message,
            "data": {}
        })
