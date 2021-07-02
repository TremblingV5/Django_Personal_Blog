from apps.manager.utils.api import ManageAbstractApiView as AbstractApiView
from apps.manager.utils.CommonApi import CommonApi
from django.http import JsonResponse
from django.template import loader
from django.forms.models import model_to_dict
from apps.manager.models import ContactInfo
from apps.manager.serializers.contactInfo import ContactInfoSerializer


class ContactInfoApi(CommonApi):

    TEMPLATE = "manage/contactInfo.html"
    TARGET = ContactInfo


class ModifyContactInfoApi(AbstractApiView):
    def get_solution(self, requests):
        code = 200
        message = "Success"
        data = {}

        record_id = requests.GET.get('id')

        if record_id != None:
            exists = ContactInfo.objects.filter(id=record_id)
            if len(exists) == 1:
                data = exists[0]

        return {
            "code": code,
            "message": message,
            "data": data,
            "template": None
        }

    def post_solution(self, requests):
        code = 200
        message = "Success"

        res = ContactInfoSerializer(data=requests.data, many=False)
        if res.is_valid(raise_exception=True):
            if requests.POST.get('id') != "":
                exists = ContactInfo.objects.filter(id=requests.POST.get('id'))
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
        exists = ContactInfo.objects.filter(id=id)
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
