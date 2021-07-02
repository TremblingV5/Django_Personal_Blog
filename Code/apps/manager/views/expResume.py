from apps.manager.utils.api import ManageAbstractApiView as AbstractApiView
from apps.manager.utils.CommonApi import CommonApi
from django.http import JsonResponse
from django.template import loader
from django.forms.models import model_to_dict
from apps.resume.models import Resume
from apps.resume.serializers.Resume import ResumeSerializer


class ExpResumekApi(CommonApi):

    TEMPLATE = "manage/expResume.html"
    TARGET = Resume


class ModifyExpResumeApi(AbstractApiView):

    CODE = 200

    def get_solution(self, requests):
        self.TEMPLATE = "manage/modifyExpResume.html"
        data = {}

        record_id = requests.GET.get('id')

        if record_id != None:
            exists = Resume.objects.filter(id=record_id)
            if len(exists) == 1:
                data = exists[0]

        return {
            "data": data
        }

    def post_solution(self, requests):
        self.TEMPLATE = "manage/200.html"

        res = ResumeSerializer(data=requests.data, many=False)
        if res.is_valid(raise_exception=True):
            if requests.POST.get('id') != "":
                exists = Resume.objects.filter(id=requests.POST.get('id'))
                res.update(exists[0], res.data)
            else:
                res.create(res.data)

        return

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
