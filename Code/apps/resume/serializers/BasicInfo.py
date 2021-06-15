from apps.resume.models import BasicInfo
from rest_framework import serializers


class BasicInfoSerializer(serializers.ModelSerializer):
    # personalImage = serializers.ImageField()

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        return BasicInfo.objects.create(**validated_data)

    def update(self, instance, validated_data, personalImage, personalQRCode):
        # return BasicInfo.objects.filter(id=instance.id).update(**validated_data)
        item = BasicInfo.objects.filter(id=instance.id)[0]
        item.name = validated_data['name']
        item.title = validated_data['title']
        item.introduction = validated_data['introduction']
        item.birthday = validated_data['birthday']
        item.mobile = validated_data['mobile']
        item.email = validated_data['email']
        item.website = validated_data['website']
        item.address = validated_data['address']
        if personalImage != None:
            item.personalImage = personalImage
        if personalQRCode != None:
            item.personalQRCode = personalQRCode
        item.is_using = validated_data['is_using']
        item.is_deleted = validated_data['is_deleted']
        return item.save()

    class Meta:
        model = BasicInfo
        fields = ('id', 'name', 'title', 'introduction', 'birthday', 'mobile', 'email', 'website', 'address',
                  'personalImage', 'personalQRCode',
                'is_using', 'is_deleted')
