from apps.manager.utils.CommonApi import CommonApi
from apps.manager.utils.ModifyApi import ModifyApi
from apps.resume.models import BasicInfo
from apps.resume.serializers.BasicInfo import BasicInfoSerializer

class ResumeInfoApi(CommonApi):

    TEMPLATE = "manage/resumeInfo.html"
    TARGET = BasicInfo


class AddResumeInfoApi(ModifyApi):

    CODE = 200
    TEMPLATE = "manage/addResumeInfo.html"
    TARGET = BasicInfo
    SERIALIZER = BasicInfoSerializer

    def post_solution(self, requests):
        self.TEMPLATE = "manage/200.html"

        res = BasicInfoSerializer(data=requests.data, many=False)
        if res.is_valid(raise_exception=True):
            if requests.POST.get('id') != "":
                exists = BasicInfo.objects.filter(id=requests.POST.get('id'))
                res.update(exists[0], res.data, requests.FILES.get('personalImage'), requests.FILES.get('personalQRCode'))
            else:
                res.create(res.data)
        return
