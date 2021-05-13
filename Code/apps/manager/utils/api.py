from utils.api import AbstractApiView
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from PersonalBlog.settings import SITE_CONFIG
from django.core.cache import cache, caches
from rest_framework import exceptions
from hashlib import md5
import time, datetime

class ManageAbstractApiView(AbstractApiView):
    """
    不要重写 post, get两个方法
    """
    def post(self, requests):
        token = requests.COOKIES['token']
        if token != None:
            info = caches['tokenPool'].get(token)
            if not info:
                return HttpResponseRedirect('/manage/login/')
        else:
            return HttpResponseRedirect('/manage/login/')

        result = self.post_solution(requests)
        type = requests.POST.get("type")
        if type == "json":
            response = JsonResponse({
                "code": result["code"],
                "message": result["message"],
                "data": result["data"]
            })
        else:
            response = HttpResponse(
                result["template"].render({
                    "code": result["code"],
                    "message": result["message"],
                    "data": result["data"],
                    "config": SITE_CONFIG
                }, requests)
            )
        new_token = md5(str(time.time()).encode('utf-8')).hexdigest()
        response.set_cookie("token", new_token, expires=datetime.datetime.now() + datetime.timedelta(hours=2))
        caches['tokenPool'].set(new_token, True, 2 * 60 * 60)
        return response

    def get(self, requests):
        try:
            token = requests.COOKIES['token']
        except:
            return HttpResponseRedirect('/manage/login/')


        if token != None:
            info = caches['tokenPool'].get(token)
            if not info:
                return HttpResponseRedirect('/manage/login/')
            else:
                caches['tokenPool'].delete(token)
        else:
            return HttpResponseRedirect('/manage/login/')

        result = self.get_solution(requests)
        type = requests.GET.get("type")
        if type == "json":
            response = JsonResponse({
                "code": result["code"],
                "message": result["message"],
                "data": result["data"]
            })
        else:
            response = HttpResponse(
                result["template"].render({
                    "code": result["code"],
                    "message": result["message"],
                    "data": result["data"],
                    "config": SITE_CONFIG
                }, requests)
            )

        new_token = md5(str(time.time()).encode('utf-8')).hexdigest()
        response.set_cookie("token", new_token, expires=datetime.datetime.now() + datetime.timedelta(hours=2))
        caches['tokenPool'].set(new_token, True, 2 * 60 * 60)
        return response

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
