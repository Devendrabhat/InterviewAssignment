from django import forms

class LinkForm(forms.Form):
    link = forms.CharField(label='Enter Your link', max_length=100)

