from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from .models import Register
from django.forms import fields, models, widgets
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth import password_validation


class RegistrationForm(UserCreationForm):
    email = forms.CharField(required=True, widget=forms.EmailInput
                            (attrs={'placeholder': 'Email','class': 'form-control'}))
    password1 = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput
                               (attrs={'placeholder': 'Password', 'class': 'form-control'}))
    password2 = forms.CharField(label=_("Confirm Password"), strip=False, widget=forms.PasswordInput
                               (attrs={'placeholder': 'Confirm Password', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        lables = {'email': 'Email'}
        widgets = {'username': forms.TextInput(
            attrs={'placeholder': 'Username', 'autofocus': True, 'class': 'form-control'})}


    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'A user with that email already exists.')
        return email

class UserAddressForm(forms.ModelForm):
    address = forms.CharField(required=True, widget=forms.TextInput
                            (attrs={'placeholder': 'Address','class': 'form-control'}))

    class Meta:
        model = Register
        fields = ['address']
        lables = {'address': 'Address'}

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput
                             (attrs={'placeholder': 'Username','autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput
                               (attrs={'placeholder': 'Password','autocomplete': 'current-password', 'class': 'form-control'}))

class EditForm(forms.ModelForm):
    email = forms.CharField(required=True, widget=forms.EmailInput
                            (attrs={'placeholder': 'Email','class': 'form-control'}))

    class Meta:
        model = User
        fields = ['email']
        lables = {'email': 'Email'}
    
