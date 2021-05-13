from apps.resume.models import CapabilityStack
from rest_framework import serializers


class CapabilityStackSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        return CapabilityStack.objects.create(**validated_data)

    def update(self, instance, validated_data):
        return CapabilityStack.objects.filter(id=instance.id).update(**validated_data)

    class Meta:
        model = CapabilityStack
        fields = '__all__'