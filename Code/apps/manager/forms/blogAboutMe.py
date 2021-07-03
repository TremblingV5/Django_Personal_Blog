from django import forms

from apps.blog.models import AboutMe


class blogAboutMeMDEditorModleForm(forms.ModelForm):
    class Meta:
        model = AboutMe
        fields = '__all__'