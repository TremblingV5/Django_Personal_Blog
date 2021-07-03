from django.forms.models import model_to_dict

from apps.manager.models import AdminUser
from apps.manager.serializers.adminInfo import AdminUserSerializer
from apps.manager.utils.api import ManageAbstractApiView as AbstractApiView


class AdminInfoApi(AbstractApiView):

    CODE = 200
    TEMPLATE = "manage/adminInfo.html"

    def get_solution(self, requests):
        exists = AdminUser.objects.filter()

        return {
            "data": model_to_dict(exists[0])
        }

    def post_solution(self, requests):

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
            "data": model_to_dict(exists[0])
        }
