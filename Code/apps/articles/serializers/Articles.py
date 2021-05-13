from apps.articles.models import Articles
from rest_framework import serializers


class ArticlesSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        return Articles.objects.create(**validated_data)

    def update(self, instance, validated_data, img_obj):
        item = Articles.objects.filter(id=instance.id)[0]
        item.title = validated_data['title']
        item.introduction = validated_data['introduction']
        item.content = validated_data['content']
        if img_obj != None:
            item.coverImage = img_obj
        item.in_turn = validated_data['in_turn']
        item.is_using = validated_data['is_using']
        item.is_deleted = validated_data['is_deleted']
        item.cate_id = validated_data['cate_id']
        return item.save()

    class Meta:
        model = Articles
        fields = '__all__'