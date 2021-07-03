from apps.blog.utils.api import BlogAbstractApiView as AbstractApiView


class IndexApi(AbstractApiView):

    CODE = 200
    TEMPLATE = "blog/index.html"

    def get_solution(self, requests):
        return {
            "data": []
        }
