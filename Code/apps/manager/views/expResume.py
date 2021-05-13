from apps.manager.utils.api import ManageAbstractApiView as AbstractApiView
from django.http import JsonResponse
from django.template import loader
from django.forms.models import model_to_dict
from apps.resume.models import Resume
from apps.resume.serializers.Resume import ResumeSerializer

class ExpResumekApi(AbstractApiView):
    def get_solution(self, requests):
        code = 200
        message = "Success"

        exists = Resume.objects.filter(is_deleted=False)

        return {
            "code": code,
            "message": message,
            "data": [model_to_dict(exists[i]) for i in range(len(exists))],
            "template": loader.get_template("manage/expResume.html")
        }

    def post_solution(self, requests):
        code = 200
        message = "Success"


        return {
            "code": code,
            "message": message,
            "data": {},
            "template": loader.get_template("manage/modifyExpResume.html")
        }

class ModifyExpResumeApi(AbstractApiView):
    def get_solution(self, requests):
        code = 200
        message = "Success"
        data = {}

        record_id = requests.GET.get('id')

        if record_id != None:
            exists = Resume.objects.filter(id=record_id)
            if len(exists) == 1:
                data = exists[0]

        return {
            "code": code,
            "message": message,
            "data": data,
            "template": loader.get_template("manage/modifyExpResume.html")
        }

    def post_solution(self, requests):
        code = 200
        message = "Success"

        res = ResumeSerializer(data=requests.data, many=False)
        if res.is_valid(raise_exception=True):
            if requests.POST.get('id') != "":
                exists = Resume.objects.filter(id=requests.POST.get('id'))
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
        exists = Resume.objects.filter(id=id)
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
