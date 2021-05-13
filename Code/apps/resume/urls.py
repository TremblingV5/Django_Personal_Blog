from django.urls import path, include
from PersonalBlog import settings
from apps.resume.views import index

# path('settask/', SetTask.SetTaskAPI.as_view(), name='settask'),
# path('download/<str:id>', files.FilesAPI.as_view(), name='download'),

urlpatterns = [
    path('', index.BasicInfoAPI.as_view(), name='personal_info'),
    path('info/', index.BasicInfoAPI.as_view(), name='personal_info')
]