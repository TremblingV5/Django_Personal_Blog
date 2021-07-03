from apps.manager.utils.CommonApi import CommonApi
from apps.manager.utils.ModifyApi import ModifyApi
from apps.resume.models import CapabilityStack
from apps.resume.serializers.CapabilityStack import CapabilityStackSerializer

class CapabilityStackApi(CommonApi):

    CODE = 200
    TEMPLATE = "manage/stackInfo.html"
    TARGET = CapabilityStack


class ModifyCapabilityStackApi(ModifyApi):

    CODE = 200
    TEMPLATE = "manage/modifyStackInfo.html"
    TARGET = CapabilityStack
    SERIALIZER = CapabilityStackSerializer
