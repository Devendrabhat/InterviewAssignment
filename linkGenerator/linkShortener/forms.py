from django import forms
from .models import LinkModel

class LinkForm(forms.Form):
    link = forms.CharField(label='Enter Your link', max_length=500)
