import datetime
import time
from hashlib import md5

from django.core.cache import caches
from django.http import HttpResponseRedirect

from utils.api import AbstractApiView


class ManageAbstractApiView(AbstractApiView):
    """
    不要重写 post, get两个方法
    """
    def request_handle(self, method, methodType, requests):
        token = requests.COOKIES.get('token')
        if not token is None:
            info = caches['tokenPool'].get(token)
            if not info:
                return HttpResponseRedirect('/manage/login/')
        else:
            return HttpResponseRedirect('/manage/login/')

        response = super().request_handle(method, methodType, requests)

        new_token = md5(str(time.time()).encode('utf-8')).hexdigest()
        response.set_cookie("token", new_token, expires=datetime.datetime.now() + datetime.timedelta(hours=2))
        caches['tokenPool'].set(new_token, True, 2 * 60 * 60)
        return response

