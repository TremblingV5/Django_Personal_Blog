from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from PersonalBlog.settings import SITE_CONFIG

class AbstractApiView(APIView):
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
                    "config": SITE_CONFIG
                }, requests)
            )

    def get(self, requests):
        result = self.get_solution(requests)
        type = requests.GET.get("type")
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
                    "config": SITE_CONFIG
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
