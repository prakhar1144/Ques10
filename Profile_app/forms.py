from django import forms
from .models import User_Detail
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User_Detail
        fields = ('name', 'email', 'picture', 'phone','location')

class Register(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')