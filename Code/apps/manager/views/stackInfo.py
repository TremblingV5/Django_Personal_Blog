from apps.manager.utils.api import ManageAbstractApiView as AbstractApiView
from django.http import JsonResponse
from django.template import loader
from django.forms.models import model_to_dict
from apps.resume.models import CapabilityStack
from apps.resume.serializers.CapabilityStack import CapabilityStackSerializer

class CapabilityStackApi(AbstractApiView):
    def get_solution(self, requests):
        code = 200
        message = "Success"

        exists = CapabilityStack.objects.filter(is_deleted=False)

        return {
            "code": code,
            "message": message,
            "data": [model_to_dict(exists[i]) for i in range(len(exists))],
            "template": loader.get_template("manage/stackInfo.html")
        }

    def post_solution(self, requests):
        code = 200
        message = "Success"


        return {
            "code": code,
            "message": message,
            "data": {},
            "template": loader.get_template("manage/modifyStackInfo.html")
        }

class ModifyCapabilityStackApi(AbstractApiView):
    def get_solution(self, requests):
        code = 200
        message = "Success"
        data = {}

        record_id = requests.GET.get('id')

        if record_id != None:
            exists = CapabilityStack.objects.filter(id=record_id)
            if len(exists) == 1:
                data = exists[0]

        return {
            "code": code,
            "message": message,
            "data": data,
            "template": loader.get_template("manage/modifyStackInfo.html")
        }

    def post_solution(self, requests):
        code = 200
        message = "Success"

        res = CapabilityStackSerializer(data=requests.data, many=False)
        if res.is_valid(raise_exception=True):
            if requests.POST.get('id') != "":
                exists = CapabilityStack.objects.filter(id=requests.POST.get('id'))
                res.update(exists[0], res.data)
            else:
                res.create(res.data)

        return {
            "code": code,
            "message": message,
            "data": {},
            "template": loader.get_template("manage/200.html")
        }

    def delete(self, requests):
        code = 0
        message = "None"

        id = requests.POST.get('id')
        exists = CapabilityStack.objects.filter(id=id)
        if len(exists) > 0:
            exists[0].is_deleted = True
            exists[0].save()
            code = 200
            message = "delete success"

        return JsonResponse({
            "code": code,
            "message": message,
            "data": {}
        })
