from rest_framework import serializers

from apps.manager.models import ContactInfo


class ContactInfoSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        return ContactInfo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        return ContactInfo.objects.filter(id=instance.id).update(**validated_data)

    class Meta:
        model = ContactInfo
        fields = '__all__'