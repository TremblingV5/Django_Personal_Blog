from rest_framework import serializers

from apps.manager.models import AdminUser
from utils.hasher import get_md5


class AdminUserSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        """
        全局验证方法
        :param attrs:
        :return:
        """

        # 若有不需要的键值对，可通过如下方法删除
        # FIXED: 不需要在此处删除
        # del attrs['passwordAgain']
        # del attrs['validate']
        attrs['password'] = get_md5(attrs['password'])
        return attrs

    def create(self, validated_data):
        return AdminUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        return AdminUser.objects.filter(id=instance.id).update(**validated_data)

    class Meta:
        model = AdminUser
        fields = ('username', 'password', 'email', 'mobile', 'name')