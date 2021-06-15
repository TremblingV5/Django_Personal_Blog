from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.core.cache import cache, caches
from apps.manager.models import AdminUser
from utils.hasher import get_md5
import time
import datetime
from django.conf import settings

class LoginApi(APIView):
    def get(self, requests):
        code = 200
        message = "Success"
        data = {
            "config": settings.SITE_CONFIG
        }

        return HttpResponse(loader.get_template("manage/login.html").render(data))


    def post(self, requests):
        code = 500
        message = "Success"
        data = {}

        item = AdminUser.objects.filter(username=requests.POST.get('username'))
        if len(item) > 0:
            password = item[0].password
            if password == requests.POST.get('password'):
                code = 200
            else:
                code = 500

        response = JsonResponse({
            "code": code
        })

        new_token = get_md5(str(time.time()))
        response.set_cookie("token", new_token, expires=datetime.datetime.now() + datetime.timedelta(hours=2))
        caches['tokenPool'].set(new_token, True, 2 * 60 * 60)

        return response

class LogoutApi(APIView):
    def get(self, requests):
        response = HttpResponseRedirect('/manage/login/')
        response.set_cookie("token", "", expires=datetime.datetime.now() + datetime.timedelta(hours=2))
        return response
