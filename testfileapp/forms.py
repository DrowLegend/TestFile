from django import forms
from testfileapp.models import User, UploadFile


class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput())
    email = forms.EmailField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email')


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = ('file',)
