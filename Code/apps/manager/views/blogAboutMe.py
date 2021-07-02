from apps.manager.utils.api import ManageAbstractApiView as AbstractApiView
from django.template import loader
from apps.blog.serializers.AboutMe import AboutMeSerializer
from apps.blog.models import AboutMe
import markdown
from apps.manager.forms.blogAboutMe import blogAboutMeMDEditorModleForm

class BlogAboutMeApi(AbstractApiView):

    CODE = 200
    TEMPLATE = "manage/blogAboutMe.html"

    def get_solution(self, requests):
        id = requests.GET.get('id')
        if id != None and id != "":
            exists = AboutMe.objects.filter(id=id, is_deleted=False)
        else:
            exists = AboutMe.objects.filter(is_deleted=False)

        if len(exists) > 0:
            data = exists[0]
        else:
            data = {
                "id": None,
                "content": "",
                "is_using": False
            }

        form = blogAboutMeMDEditorModleForm(instance=data)

        return {
            "data": {
                "data": data,
                "form": form
            }
        }

    def post_solution(self, requests):
        form = AboutMeSerializer(data=requests.data, many=False)
        if form.is_valid(raise_exception=True):
            form.update(requests.POST.get('id'), form.data)

        exists = AboutMe.objects.filter(id=requests.POST.get('id'), is_deleted=False)

        form = blogAboutMeMDEditorModleForm(instance=exists[0])

        return {
            "data": {
                "data": exists[0],
                "form": form
            }
        }

