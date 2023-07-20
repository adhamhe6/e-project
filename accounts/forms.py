from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
    full_name = forms.CharField(max_length=255)
    email = forms.EmailField(validators=[validate_email])

    class Meta:
        model = User
        fields = ['full_name', 'email', 'password1', 'password2']
        
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError('This email address is already in use.')
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name, user.last_name = self.cleaned_data['full_name'].split(maxsplit=1)
        user.username = user.first_name
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            UserProfile.objects.create(user=user, full_name=self.cleaned_data['full_name'], email=user.email)
        return user