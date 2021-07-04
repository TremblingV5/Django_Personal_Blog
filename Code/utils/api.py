import traceback
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from PersonalBlog.settings import SITE_CONFIG, STATUS_INFO
from django.template import loader

class AbstractApiView(APIView):
    CODE = 500
    TEMPLATE = "manage/404.html"

    def post(self, requests):
        return self.request_handle(self.post_solution, requests.POST, requests)

    def get(self, requests):
        return self.request_handle(self.get_solution, requests.GET, requests)

    def put(self, requests):
        pass

    def delete(self, requests):
        return self.request_handle(self.delete_solution, requests.POST, requests)

    def request_handle(self, method, methodType, request):
        try:
            result = method(request)
        except Exception as e:
            traceback.print_exc()
            print(e.__str__())
            self.CODE = 500
            result = {}

        self.reqType = methodType.get("type")
        responseData = {
            "code": self.CODE,
            "message": STATUS_INFO[self.CODE],
            "data": result["data"] if result not in [None, {}] else {},
            "config": SITE_CONFIG
        }
        if self.reqType == "json":
            return JsonResponse(self.data_wrap(responseData))
        else:
            return HttpResponse(
                loader.get_template(self.TEMPLATE).render(self.data_wrap(responseData), request)
            )

    def data_wrap(self, responseData):
        return

    def post_solution(self, requests):
        pass

    def get_solution(self, requests):
        pass

    def delete_solution(self, requests):
        pass