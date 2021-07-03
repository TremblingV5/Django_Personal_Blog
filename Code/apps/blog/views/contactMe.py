from apps.blog.utils.api import BlogAbstractApiView as AbstractApiView


class ContactMeApi(AbstractApiView):

    CODE = 200
    TEMPLATE = "blog/contactMe.html"
