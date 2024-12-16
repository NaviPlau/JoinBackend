from django.db import models
from django.contrib.auth.models import AbstractUser
import random


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, error_messages={
            'unique': ('Email already taken.') },)
    username = models.CharField(max_length=150, help_text="Required. Must contain exactly two words.")
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    fullname = models.CharField(max_length=255)
    initials = models.CharField(max_length=5)
    initialsColor = models.CharField(max_length=7)
    phone = models.CharField(max_length=255, default="123456704343")
    email = models.EmailField(unique=True) 
    selected = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.fullname}'s Profile"

    def save(self, *args, **kwargs):
        if len(self.fullname.split()) != 2:
            raise ValueError("Fullname must contain exactly two words.")
        first_name, last_name = self.fullname.split()
        self.initials = f"{first_name[0].upper()}{last_name[0].upper()}"
        if not self.initialsColor:
            self.initialsColor = f"#{random.randint(0, 0xFFFFFF):06x}"
        if self.user.email != self.email:
            self.email = self.user.email

        super().save(*args, **kwargs)


