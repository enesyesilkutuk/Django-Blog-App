from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Userprofile

class UserForm(UserCreationForm): # Register sayfasının üst kısmı için oluşturduk
    class Meta:
        model = User
        fields =["username", "email"]
        help_texts = {
            'username': None,
            'password': None,
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Userprofile
        exclude = ('user',)
        # fields = ['portfolio', 'profile_pic']


# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields =["username", "email"]
       