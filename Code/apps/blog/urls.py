from django.urls import path

from apps.blog.views import index, aboutMe, timeline, blogsCategory, article, contactMe

# path('settask/', SetTask.SetTaskAPI.as_view(), name='settask'),
# path('download/<str:id>', files.FilesAPI.as_view(), name='download'),

urlpatterns = [
    path('', index.IndexApi.as_view(), name='blog_index'),
    path('index/', index.IndexApi.as_view(), name='blog_index'),
    path('about/', aboutMe.AboutMeApi.as_view(), name='aboutMe'),
    path('getAboutMe/', aboutMe.GetAboutMeApi.as_view(), name='getAboutMe'),
    path('timeline/', timeline.TimelineApi.as_view(), name='timeline'),
    path('category/', blogsCategory.BlogCategoryApi.as_view(), name='category'),
    path('article/<int:article_id>', article.ArticleApi.as_view(), name='article'),
    path('contactMe/', contactMe.ContactMeApi.as_view(), name='blogContactMe')
]