from apps.manager.utils.api import ManageAbstractApiView as AbstractApiView
from django.template import loader


class ManagerIndexApi(AbstractApiView):
    def get_solution(self, requests):
        code = 200
        message = "Success"
        data = {}

        return {
            "code": code,
            "message": message,
            "data": data,
            "template": loader.get_template("manage/base.html")
        }
