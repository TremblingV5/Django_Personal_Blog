from django import forms

from mdeditor.fields import MDTextFormField
from apps.blog.models import AboutMe


class blogAboutMeMDEditorModleForm(forms.ModelForm):
    class Meta:
        model = AboutMe
        fields = '__all__'