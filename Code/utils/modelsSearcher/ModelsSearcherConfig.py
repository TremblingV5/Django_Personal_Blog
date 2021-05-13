from apps.articles import models as articlesModels
from apps.blog import models as blogModels
from apps.manager import models as managerModels
from apps.resume import models as resumeModels
from apps.articles import serializers as articlesSerializers
from apps.blog import serializers as blogSerializers
from apps.manager import serializers as managerSerializers
from apps.resume import serializers as resumeSerializers

class ModelsSearcherConfig:
    config = {
        "Articles": {
            "model": articlesModels.Articles(),
            "serializer": articlesSerializers.Articles.ArticlesSerializer()
        },
        "ArticleCategories": {
            "models": articlesModels.ArticleCategories(),
            "serializer": articlesSerializers.ArticleCategories.ArticleCategoriesSerializer()
        },
        "AboutMe": {
            "models": blogModels.AboutMe(),
            "serializer": blogSerializers.AboutMe.AboutMeSerializer()
        },
        "AdminUser": {
            "models": managerModels.AdminUser(),
            "serializer": managerSerializers.adminInfo.AdminUserSerializer()
        },
        "ContactInfo": {
            "models": managerModels.ContactInfo(),
            # "serializer": managerSerializers.contactInfo.ContactInfoSerializer()
        },
        "BasicInfo": {
            "models": resumeModels.BasicInfo(),
            "serializer": resumeSerializers.BasicInfo.BasicInfoSerializer()
        },
        "Resume": {
            "models": resumeModels.Resume(),
            "serializer": resumeSerializers.Resume.ResumeSerializer()
        },
        "CapabilityStack": {
            "models": resumeModels.CapabilityStack(),
            "serializer": resumeSerializers.CapabilityStack.CapabilityStackSerializer()
        },
        "Projects": {
            "models": resumeModels.Projects()
        }
    }

