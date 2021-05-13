from apps.blog.utils.api import BlogAbstractApiView as AbstractApiView
from apps.articles.models import Articles
from apps.articles.serializers.Articles import ArticlesSerializer
from django.http import JsonResponse
from utils.paginator import ArticleCategoryPagePagination
from django.template import loader
from django.forms.models import model_to_dict

class BlogCategoryApi(AbstractApiView):
    def get_solution(self, requests):
        code = 200
        message = "Success"

        paginator = ArticleCategoryPagePagination()
        exists = Articles.objects.filter(is_deleted=False).order_by("-update_time")

        cate = []
        data = [model_to_dict(exists[i]) for i in range(len(exists))]
        for i in range(len(exists)):
            data[i]['cate_id'] = exists[i].cate_id.name
            data[i]['coverImage'] = data[i]['coverImage'].name
            if exists[i].cate_id.name not in cate:
                cate.append("%s" % exists[i].cate_id.name)

        data, num_pages = paginator.paginate_queryset(data, requests, view=self)

        return {
            "code": code,
            "message": message,
            "data": {
                "data": data,
                "category": cate,
                'cate': " ".join(cate)
            },
            "template": loader.get_template("blog/blogCategory.html")
        }

    def post_solution(self, requests):
        code = 200
        message = "Success"


        return {
            "code": code,
            "message": message,
            "data": {},
            "template": loader.get_template("blog/blogCategory.html")
        }