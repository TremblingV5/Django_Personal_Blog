from django.urls import path

from apps.manager.views import articles, contactInfo
from apps.manager.views import index, login, adminInfo, resumeInfo, stackInfo, blogAboutMe, expResume, articleCategory

# path('settask/', SetTask.SetTaskAPI.as_view(), name='settask'),
# path('download/<str:id>', files.FilesAPI.as_view(), name='download'),

urlpatterns = [
    path('workbench/', index.ManagerIndexApi.as_view(), name='workbench'),
    path('login/', login.LoginApi.as_view(), name='login'),
    path('logout/', login.LogoutApi.as_view(), name='logout'),
    path('adminInfo/', adminInfo.AdminInfoApi.as_view(), name='adminInfo'),
    path('addResumeInfo/', resumeInfo.AddResumeInfoApi.as_view(), name='addResumeInfo'),
    path('resumeInfo/', resumeInfo.ResumeInfoApi.as_view(), name='resumeInfo'),
    path('stackInfo/', stackInfo.CapabilityStackApi.as_view(), name='stackInfo'),
    path('modifyStackInfo/', stackInfo.ModifyCapabilityStackApi.as_view(), name='modifyStackInfo'),
    path('blogAboutMe/', blogAboutMe.BlogAboutMeApi.as_view(), name='blogAboutMe'),
    path('expResume/', expResume.ExpResumekApi.as_view(), name='expResume'),
    path('modifyExpResume/', expResume.ModifyExpResumeApi.as_view(), name='modifyExpResume'),
    path('articleCategory/', articleCategory.ArticleCategoryApi.as_view(), name='articleCategory'),
    path('modifyArticleCategory/', articleCategory.ModifyArticleCategoryApi.as_view(), name='modifyArticleCategory'),
    path('articles/', articles.ArticlesApi.as_view(), name='articles'),
    path('modifyArticles/', articles.ModifyArticlesApi.as_view(), name='modifyArticles'),
    path('contactInfo/', contactInfo.ContactInfoApi.as_view(), name='contactInfo'),
    path('modifyContactInfo/', contactInfo.ModifyContactInfoApi.as_view(), name='modifyContactInfo')

]