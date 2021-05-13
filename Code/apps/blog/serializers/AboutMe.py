from apps.blog.models import AboutMe
from rest_framework import serializers


class AboutMeSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        return AboutMe.objects.create(**validated_data)

    def update(self, id, validated_data):
        return AboutMe.objects.filter(id=id).update(**validated_data)

    class Meta:
        model = AboutMe
        fields = '__all__'