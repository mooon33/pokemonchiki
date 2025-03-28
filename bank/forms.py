from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import User_reg


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    account_number = forms.CharField(max_length=20, required=True)
    phone = forms.CharField(max_length=15, required=True)
    account_type = forms.ChoiceField(choices=User_reg.ACCOUNT_TYPES, required=True)
    gender = forms.ChoiceField(choices=User_reg.GENDER_CHOICES, required=True)
    address = forms.CharField(max_length=200, required=True)
    photo = forms.ImageField(required=False)
    pan = forms.CharField(max_length=20, required=True)
    aadhaar = forms.CharField(max_length=20, required=True)
    dob = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')