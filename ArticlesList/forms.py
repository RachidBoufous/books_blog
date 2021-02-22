from django import forms
from . import models

class createArticle(forms.ModelForm):
    class Meta:
        model = models.Articles
        fields = ['Title','slug','body','Logo']