from apps.manager.utils.api import ManageAbstractApiView as AbstractApiView
from django.http import JsonResponse
from django.template import loader
from django.forms.models import model_to_dict
from apps.resume.models import BasicInfo
from apps.resume.serializers.BasicInfo import BasicInfoSerializer

class ResumeInfoApi(AbstractApiView):
    def get_solution(self, requests):
        code = 200
        message = "Success"

        exists = BasicInfo.objects.filter(is_deleted=False)
        print([model_to_dict(exists[i]) for i in range(len(exists))])

        return {
            "code": code,
            "message": message,
            "data": [model_to_dict(exists[i]) for i in range(len(exists))],
            "template": loader.get_template("manage/resumeInfo.html")
        }

    def post_solution(self, requests):
        code = 200
        message = "Success"


        return {
            "code": code,
            "message": message,
            "data": {},
            "template": loader.get_template("manage/addResumeInfo.html")
        }

class AddResumeInfoApi(AbstractApiView):
    def get_solution(self, requests):
        code = 200
        message = "Success"
        data = {}

        record_id = requests.GET.get('id')

        if record_id != None:
            exists = BasicInfo.objects.filter(id=record_id)
            if len(exists) == 1:
                data = exists[0]

        return {
            "code": code,
            "message": message,
            "data": data,
            "template": loader.get_template("manage/addResumeInfo.html")
        }

    def post_solution(self, requests):
        code = 200
        message = "Success"

        res = BasicInfoSerializer(data=requests.data, many=False)
        if res.is_valid(raise_exception=True):
            print(res.data)
            if requests.POST.get('id') != "":
                exists = BasicInfo.objects.filter(id=requests.POST.get('id'))
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
        exists = BasicInfo.objects.filter(id=id)
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
