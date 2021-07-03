from rest_framework import serializers

from apps.articles.models import ArticleCategories


class ArticleCategoriesSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        return ArticleCategories.objects.create(**validated_data)

    def update(self, instance, validated_data):
        return ArticleCategories.objects.filter(id=instance.id).update(**validated_data)

    class Meta:
        model = ArticleCategories
        fields = '__all__'