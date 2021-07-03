from django.urls import path

from apps.resume.views import index

# path('settask/', SetTask.SetTaskAPI.as_view(), name='settask'),
# path('download/<str:id>', files.FilesAPI.as_view(), name='download'),

urlpatterns = [
    path('', index.BasicInfoAPI.as_view(), name='personal_info'),
    path('info/', index.BasicInfoAPI.as_view(), name='personal_info')
]