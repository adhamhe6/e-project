from django.db import models
from django.contrib.auth.models import User
from django.core.validators import validate_email

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, validators=[validate_email])
    profile_image = models.ImageField(upload_to='accounts/profile_images/', default='user.png', blank=True, null=True)

    def __str__(self):
        return self.user.username
  
"""from django.contrib.auth.models import AbstractUser
 from django.core.exceptions import ValidationError
from creditcard import validate_card_number
from django.contrib.auth.models import User
from django.core.validators import CreditCardValidator """

""" class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, validators=[validate_email])
    profile_image = models.ImageField(upload_to='accounts/profile_images/', default='user.png', blank=True, null=True)

    def __str__(self):
        return self.username """

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
#     full_name = pass
#     email = pass
#     profil_image = pass
#     info = pass
    
""" class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts')
    title = models.CharField(max_length=50, choices=[('primary', 'Primary'), ('secondary', 'Secondary')], default='primary')
    number = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses')
    title = models.CharField(max_length=50, choices=[('home', 'Home'), ('office', 'Office'), ('business', 'Business'), ('academy', 'Academy'), ('others', 'Others')], default='home')
    address = models.TextField()

    def __str__(self):
        return self.title

def validate_credit_card_number(value):
    if not validate_card_number(value):
        raise ValidationError('Invalid credit card number')

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments')
    card_number = models.CharField(max_length=20, validators=[CreditCardValidator(), validate_credit_card_number])

    def __str__(self):
        return self.card_number """