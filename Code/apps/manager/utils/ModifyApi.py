from apps.manager.utils.api import AbstractApiView


class ModifyApi(AbstractApiView):

    CODE = 200
    TARGET = None
    SERIALIZER = None

    def get_solution(self, requests):
        record_id = requests.GET.get('id')
        if record_id is not None:
            exists = self.TARGET.objects.filter(id=record_id)
            if len(exists) == 1:
                return {
                    "data": exists[0]
                }
        return

    def post_solution(self, requests):
        self.TEMPLATE = "manage/200.html"
        res = self.SERIALIZER(data=requests.data, many=False)
        if res.is_valid(raise_exception=True):
            if requests.POST.get('id') != "":
                exists = self.TARGET.objects.filter(id=requests.POST.get('id'))
                res.update(exists[0], res.data)
            else:
                res.create(res.data)
        return

    def delete_solution(self, requests):
        exists = self.TARGET.objects.filter(id=requests.POST.get('id'))
        if len(exists) > 0:
            exists[0].is_deleted = True
            exists[0].is_using = False
            exists[0].in_turn = False
            exists[0].save()
        return