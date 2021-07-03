from apps.articles.models import ArticleCategories
from apps.articles.serializers.ArticleCategories import ArticleCategoriesSerializer
from apps.manager.utils.CommonApi import CommonApi
from apps.manager.utils.ModifyApi import ModifyApi


class ArticleCategoryApi(CommonApi):

    TEMPLATE = "manage/articleCategory.html"
    TARGET = ArticleCategories


class ModifyArticleCategoryApi(ModifyApi):

    CODE = 200
    TEMPLATE = "manage/modifyArticleCategory.html"
    TARGET = ArticleCategories
    SERIALIZER = ArticleCategoriesSerializer
