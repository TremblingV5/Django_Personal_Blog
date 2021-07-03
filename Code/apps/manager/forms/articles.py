from django import forms

from apps.articles.models import Articles


class ArticlesMDEditorModleForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = '__all__'