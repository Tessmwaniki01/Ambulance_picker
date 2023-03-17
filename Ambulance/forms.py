from django import forms
from . models import *
from django.contrib.auth.forms import UserCreationForm

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        
#ambulance update form
class AmbulanceUpdateForm(forms.ModelForm):
    class Meta:
        model = Ambulance
        exclude = ['owner_id']
     
#comments form
class CommentForm(forms.ModelForm):
     class Meta:
        model = Feedback
        fields=['user_name','email', 'content', 'rating']
        
class OrderForm(forms.ModelForm):
     class Meta:
        model = Order
        exclude=['user_id','ambulance_id']
        
        
class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",'data-toggle': 'password',
                 'id': 'password',
            }
        )
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",'data-toggle': 'password',
                 'id': 'password',
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",'data-toggle': 'password',
                 'id': 'password',
                
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_admin', 'is_owner', 'is_public')