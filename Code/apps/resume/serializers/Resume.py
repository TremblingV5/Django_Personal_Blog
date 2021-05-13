from apps.resume.models import Resume
from rest_framework import serializers


class ResumeSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        return Resume.objects.create(**validated_data)

    def update(self, instance, validated_data):
        return Resume.objects.filter(id=instance.id).update(**validated_data)

    class Meta:
        model = Resume
        fields = '__all__'