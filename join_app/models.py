from django.db import models
from join_auth.models import CustomUser, UserProfile
from django.contrib.auth import get_user_model
import random

User = get_user_model()

class Contact(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='contacts'
    )
    email = models.EmailField()
    fullname = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    initials = models.CharField(max_length=5, blank=True)  
    initialsColor = models.CharField(max_length=7, blank=True)

    def save(self, *args, **kwargs):
        if len(self.fullname.split()) != 2:
            raise ValueError("Fullname must contain exactly two words.")
        self.initials = ''.join([name[0].upper() for name in self.fullname.split()[:2]])
        if not self.initialsColor:
            self.initialsColor = f"#{random.randint(0, 0xFFFFFF):06x}"
        super().save(*args, **kwargs)  

    def __str__(self):
        return f"{self.fullname} ({self.email})"
    
    

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('urgent', 'Urgent'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]

    CATEGORY_CHOICES = [
        ('Technical Task', 'Technical Task'),
        ('User Story', 'User Story'),
    ]

    COLUMN_CHOICES = [
        ('toDo', 'To Do'),
        ('awaitingFeedback', 'Awaiting Feedback'),
        ('inProgress', 'In Progress'),
        ('done', 'Done'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    dueDate = models.DateField()
    subtasks = models.JSONField(default=list) 
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    column = models.CharField(max_length=20, choices=COLUMN_CHOICES)
    assignedTo = models.ManyToManyField(UserProfile, related_name='tasks') 

    def __str__(self):
        return self.title

