from utils.api import AbstractApiView
from django.template import loader
from apps.resume.models import BasicInfo, Resume, CapabilityStack
from apps.resume.serializers.BasicInfo import BasicInfoSerializer
from apps.resume.serializers.Resume import ResumeSerializer
from apps.resume.serializers.CapabilityStack import CapabilityStackSerializer

class BasicInfoAPI(AbstractApiView):
    def get_solution(self, requests):
        code = 200
        message = "Success"
        data = {}

        try:
            queryset = BasicInfo.objects.filter(is_using=1, is_deleted=False)
            result = BasicInfoSerializer(queryset, many=True)
            aboutMe = result.data[0]
        except:
            code = 404
            message = "Get personal information defeat"
            aboutMe = {}

        try:
            queryset = Resume.objects.filter(is_using=1, type="edu", is_deleted=False).order_by('-start_time')
            result = ResumeSerializer(queryset, many=True)
            eduResume = result.data
        except:
            eduResume = {}

        try:
            queryset = Resume.objects.filter(is_using=1, type="job", is_deleted=False).order_by('-start_time')
            result = ResumeSerializer(queryset, many=True)
            jobResume = result.data
        except:
            jobResume = {}

        try:
            queryset = CapabilityStack.objects.filter(is_using=1, is_deleted=False).order_by('-rate')
            if len(queryset) > 7:
                queryset = queryset[:7]
            result = CapabilityStackSerializer(queryset, many=True)
            stackInfo = result.data
            backgroundList = [
                "#D37091", "#B16DB2", "#6D75C8", "#007BC8", "#007BAA", "#007575", "#FF9778"
            ]
            for i in range(len(stackInfo)):
                stackInfo[i]['background'] = backgroundList[i]
        except:
            stackInfo = {}

        return {
            "code": code,
            "message": message,
            "data": {
                "about": aboutMe,
                'eduResume': eduResume,
                'jobResume': jobResume,
                'stackInfo': stackInfo
            },
            "template": loader.get_template("resume/base.html")
        }
