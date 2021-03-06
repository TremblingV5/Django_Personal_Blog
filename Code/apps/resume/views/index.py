from apps.resume.models import BasicInfo, Resume, CapabilityStack
from apps.resume.serializers.BasicInfo import BasicInfoSerializer
from apps.resume.serializers.CapabilityStack import CapabilityStackSerializer
from apps.resume.serializers.Resume import ResumeSerializer
from apps.articles.models import Articles
from apps.articles.serializers.Articles import ArticlesSerializer
from utils.api import AbstractApiView


class BasicInfoAPI(AbstractApiView):

    CODE = 200
    TEMPLATE = "resume/base.html"

    def data_wrap(self, responseData):
        try:
            queryset = BasicInfo.objects.filter(is_using=1, is_deleted=False)
            result = BasicInfoSerializer(queryset, many=True)
            aboutMe = result.data[0]
        except:
            self.CODE = 404
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

        try:
            queryset = Articles.objects.filter(is_using=1, is_deleted=False).order_by('-update_time')
            if len(queryset) > 8:
                queryset = queryset[:8]
            result = ArticlesSerializer(queryset, many=True)
            recentFiles = result.data
            for i in range(len(recentFiles)):
                recentFiles[i]["update_time_formatted"] = recentFiles[i]["update_time"][:10]
        except Exception as e:
            print(e.__str__())
            recentFiles = {}

        responseData["data"] = {
            "about": aboutMe,
            'eduResume': eduResume,
            'jobResume': jobResume,
            'stackInfo': stackInfo,
            'recentFiles': recentFiles
        }

        return responseData
