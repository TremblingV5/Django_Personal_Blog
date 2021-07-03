from apps.manager.utils.CommonApi import CommonApi
from apps.manager.utils.ModifyApi import ModifyApi
from apps.resume.models import Resume
from apps.resume.serializers.Resume import ResumeSerializer


class ExpResumekApi(CommonApi):

    TEMPLATE = "manage/expResume.html"
    TARGET = Resume


class ModifyExpResumeApi(ModifyApi):

    CODE = 200
    TEMPLATE = "manage/modifyExpResume.html"
    TARGET = Resume
    SERIALIZER = ResumeSerializer