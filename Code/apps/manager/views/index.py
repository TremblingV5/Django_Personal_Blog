from apps.manager.utils.api import ManageAbstractApiView as AbstractApiView


class ManagerIndexApi(AbstractApiView):

    TEMPLATE = "manage/base.html"
