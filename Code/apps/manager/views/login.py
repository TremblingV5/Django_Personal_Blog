import datetime
import time

from django.conf import settings
from django.core.cache import caches
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from django.template import loader
from rest_framework.views import APIView

from apps.manager.models import AdminUser
from utils.hasher import get_md5


class LoginApi(APIView):
    def get(self, requests):
        data = {
            "config": settings.SITE_CONFIG
        }

        return HttpResponse(loader.get_template("manage/login.html").render(data))


    def post(self, requests):
        code = 500

        response = JsonResponse({
            "code": code
        })

        item = AdminUser.objects.filter(username=requests.POST.get('username'))
        if len(item) > 0:
            password = item[0].password
            if password == requests.POST.get('password'):
                response = JsonResponse({
                    "code": 200
                })
                new_token = get_md5(str(time.time()))
                response.set_cookie("token", new_token, expires=datetime.datetime.now() + datetime.timedelta(hours=2))
                caches['tokenPool'].set(new_token, True, 2 * 60 * 60)
            else:
                response = JsonResponse({
                    "code": 500
                })

        return response

class LogoutApi(APIView):
    def get(self, requests):
        response = HttpResponseRedirect('/manage/login/')
        response.set_cookie("token", "", expires=datetime.datetime.now() + datetime.timedelta(hours=2))
        return response
