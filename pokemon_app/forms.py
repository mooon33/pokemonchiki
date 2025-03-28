from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Application, City


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=False)
    phone = forms.CharField(required=True)
    birth_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    city = forms.ModelChoiceField(
        queryset=City.objects.all(),
        required=False
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'phone', 'password1', 'password2', 'city', 'birth_date')


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('title', 'description')