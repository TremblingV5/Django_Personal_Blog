from apps.resume.models import BasicInfo
from rest_framework import serializers


class BasicInfoSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        return BasicInfo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        return BasicInfo.objects.filter(id=instance.id).update(**validated_data)

    class Meta:
        model = BasicInfo
        fields = '__all__'