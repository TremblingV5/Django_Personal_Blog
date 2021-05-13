from apps.manager.utils.api import ManageAbstractApiView as AbstractApiView
from django.template import loader
from apps.manager.serializers.adminInfo import AdminUserSerializer
from apps.manager.models import AdminUser
from django.forms.models import model_to_dict
from django.http.request import QueryDict

class AdminInfoApi(AbstractApiView):
    def get_solution(self, requests):
        code = 200
        message = "Success"
        exists = AdminUser.objects.filter()

        return {
            "code": code,
            "message": message,
            "data": model_to_dict(exists[0]),
            "template": loader.get_template("manage/adminInfo.html")
        }

    def post_solution(self, requests):
        code = 200
        message = "Success"

        if requests.data.get('password') != requests.data.get('passwordAgain'):
            raise Exception("密码输入不一致")

        if requests.data.get('password') == "":
            raise Exception("密码输入为空")

        exists = AdminUser.objects.filter(username=requests.POST.get('username'))

        res = AdminUserSerializer(data=requests.data, many=False)

        if res.is_valid():
            if len(exists) == 0:
                res.create(res.data)
            else:
                res.update(exists[0], res.data)

        return {
            "code": code,
            "message": message,
            "data": model_to_dict(exists[0]),
            "template": loader.get_template("manage/adminInfo.html")
        }
