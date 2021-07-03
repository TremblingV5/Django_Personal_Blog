from django.forms.models import model_to_dict
from django.http import JsonResponse

from apps.articles.models import ArticleCategories
from apps.articles.models import Articles
from apps.articles.serializers.Articles import ArticlesSerializer
from apps.manager.forms.articles import ArticlesMDEditorModleForm
from apps.manager.utils.api import ManageAbstractApiView as AbstractApiView
from utils.paginator import ManagePagePagination


class ArticlesApi(AbstractApiView):

    CODE = 200
    TEMPLATE = "manage/articles.html"

    def get_solution(self, requests):

        paginator = ManagePagePagination()
        exists = Articles.objects.filter(is_deleted=False).order_by("-create_time")
        exists, num_pages = paginator.paginate_queryset(exists, requests, view=self)

        data = [model_to_dict(exists[i]) for i in range(len(exists))]
        for i in range(len(exists)):
            data[i]['cate_id'] = exists[i].cate_id.name
        return {
            "data": data
        }

class ModifyArticlesApi(AbstractApiView):

    CODE = 200

    def get_solution(self, requests):
        self.TEMPLATE = "manage/modifyArticles.html"

        id = requests.GET.get('id')

        if id != None and id != "":
            exists = Articles.objects.filter(id=id, is_deleted=False)
        else:
            exists = {}

        if len(exists) > 0:
            data = exists[0]
        else:
            data = {
                "id": None,
                "content": "",
                "is_using": False
            }

        if len(exists) > 0:
            form = ArticlesMDEditorModleForm(instance=data)
        else:
            form = ArticlesMDEditorModleForm()

        categories = ArticleCategories.objects.all()

        return {
            "data": {
                "data": data,
                "cates": categories,
                "form": form
            }
        }

    def post_solution(self, requests):
        self.TEMPLATE = "manage/200.html"

        res = ArticlesSerializer(data=requests.data, many=False)
        id = requests.POST.get('id')

        if res.is_valid(raise_exception=True):
            if id != "" and id != None and id != "None":
                exists = Articles.objects.filter(id=requests.POST.get('id'))
                data = res.data
                categories = ArticleCategories.objects.filter(id=data['cate_id'])
                data['cate_id'] = categories[0]
                data['coverImage'] = requests.FILES.get('coverImage')
                res.update(exists[0], data, requests.FILES.get('coverImage'))
            else:
                data = res.data
                categories = ArticleCategories.objects.filter(id=data['cate_id'])
                data['cate_id'] = categories[0]
                data['coverImage'] = requests.FILES.get('coverImage')
                res.create(data)

        return

    def delete(self, requests):
        code = 0
        message = "None"

        id = requests.POST.get('id')
        exists = Articles.objects.filter(id=id)
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
