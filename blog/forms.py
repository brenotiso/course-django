from django import forms
from .models import (
    Publication,
    Comment
)


class Publication_Admin(forms.ModelForm):
    class Meta:
        model = Publication
        exclude = ['author']


class Comment_Form(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
