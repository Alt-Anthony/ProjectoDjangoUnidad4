from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class NewUser(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(NewUser, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user

class Project(forms.Form):
    titulo = forms.CharField(max_length=100, required=True)
    descripcion = forms.CharField(max_length=200, required=True)
    url_foto = forms.URLField(required=True)
    tags = forms.CharField(max_length=100, required=True)
    url_github = forms.URLField(required=True)