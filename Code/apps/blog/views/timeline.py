import json

from django.core.paginator import InvalidPage, Paginator
from django.forms.models import model_to_dict
from django.http import Http404
from django.http import JsonResponse
from haystack.views import SearchView

from apps.articles.models import Articles
from apps.blog.utils.api import BlogAbstractApiView as AbstractApiView
from utils.paginator import ManagePagePagination


class TimelineApi(AbstractApiView):

    CODE = 200
    TEMPLATE = "blog/timeline.html"

    def get_solution(self, requests):
        paginator = ManagePagePagination()
        exists = Articles.objects.filter(is_deleted=False).order_by("-update_time")
        recent = [model_to_dict(exists[i]) for i in range(len(exists))][:15]
        for i in range(len(recent)):
            recent[i]['coverImage'] = recent[i]['coverImage'].url.replace("/resources", "")
            recent[i]['create_time'] = exists[i].create_time
            recent[i]['create_time_formatted'] = exists[i].create_time.strftime("%Y-%m-%d")

        exists, num_pages = paginator.paginate_queryset(exists, requests, view=self)

        if requests.GET.get('q'):
            data = json.loads(Search(results_per_page=10).__call__(requests).content)['data']
        else:
            data = [model_to_dict(exists[i]) for i in range(len(exists))]
            for i in range(len(data)):
                data[i]['coverImage'] = data[i]['coverImage'].url.replace("/resources", "")
                data[i]['create_time'] = exists[i].create_time
                data[i]['create_time_formatted'] = exists[i].create_time.strftime("%Y-%m-%d")
        return {
            "data": {
                "data": data,
                "recent": recent
            }
        }

class Search(SearchView):
    template = "blog/timeline.html"

    def create_response(self):
        context = super().get_context()
        keyword = self.request.GET.get('q', None)
        if not keyword:
            return JsonResponse({
                "status": {
                    "code": 400,
                    "msg": {
                        "error_code": 4450,
                        "error_msg": "关键字错误"
                    }
                }
            },
                json_dumps_params = {
                    'ensure_ascii': False
                }
            )
        content = {
            "status": {
                "code": 200,
                "msg": "ok"
            },
            "data": {

            }
        }
        content_dict = dict()

        return JsonResponse({"data": [{
            "id": item.object.id,
            "cate_id": item.object.cate_id.id,
            "title": item.object.title,
            "introduction": item.object.introduction,
            "content": item.object.content,
            "coverImage": item.object.coverImage.url.replace("/resources", ""),
            "in_turn": item.object.in_turn,
            "is_using": item.object.is_using,
            "is_deleted": item.object.is_deleted,
            "create_time": item.object.create_time,
            "update_time": item.object.update_time,
            "create_time_formatted": item.object.create_time.strftime("%Y-%m-%d")
        } for item in context['page'].object_list]})

    def build_page(self):
        """
        Paginates the results appropriately.

        In case someone does not want to use Django's built-in pagination, it
        should be a simple matter to override this method to do what they would
        like.
        """
        try:
            page_no = int(self.request.GET.get("p", 1))
        except (TypeError, ValueError):
            raise Http404("Not a valid number for page.")

        if page_no < 1:
            raise Http404("Pages should be 1 or greater.")

        start_offset = (page_no - 1) * self.results_per_page
        self.results = self.results.order_by("-id")
        self.results[start_offset : start_offset + self.results_per_page]

        paginator = Paginator(self.results, self.results_per_page)

        try:
            page = paginator.page(page_no)
        except InvalidPage:
            raise Http404("No such page!")

        return (paginator, page)