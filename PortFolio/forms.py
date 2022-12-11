from django import forms

class WebForm(forms.Form):
    photo = forms.URLField(max_length=200)
    title = forms.CharField(max_length=100)
    description = forms.CharField(max_length=200)     
    tags = forms.CharField(max_length=100)
    url_github = forms.URLField(max_length=200)
