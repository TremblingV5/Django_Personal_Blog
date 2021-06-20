from apps.blog.utils.api import BlogAbstractApiView as AbstractApiView
from apps.blog.models import AboutMe
from apps.articles.models import Articles
from django.http import JsonResponse
from django.template import loader
from django.forms.models import model_to_dict
import markdown

class AboutMeApi(AbstractApiView):
    def get_solution(self, requests):
        code = 200
        message = "Success"

        exists = AboutMe.objects.filter()
        content = model_to_dict(exists[0])['content']

        content = markdown.markdown(content.replace("\r\n",' \n'), extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
            'mdx_math',
        ])

        exists = Articles.objects.filter(is_deleted=False).order_by("-update_time")
        recent = [model_to_dict(exists[i]) for i in range(len(exists))]

        return {
            "code": code,
            "message": message,
            "data": {
                'content': content,
                'recent': recent[:10]
            },
            "template": loader.get_template("blog/aboutMe.html")
        }

    def post_solution(self, requests):
        code = 200
        message = "Success"


        return {
            "code": code,
            "message": message,
            "data": {},
            "template": loader.get_template("blog/aboutMe.html")
        }

class GetAboutMeApi(AbstractApiView):
    def get_solution(self, requests):
        code = 200
        message = "Success"

        exists = AboutMe.objects.filter()
        content = model_to_dict(exists[0])['content']

        content = markdown.markdown(content, extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
            'mdx-math'
        ])

        return {
            "code": code,
            "message": message,
            "data": {
                'content': content
            },
            "template": loader.get_template("blog/articlePage.html")
        }
