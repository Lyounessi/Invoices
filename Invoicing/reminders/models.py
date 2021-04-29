from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField

# Create your models here.

class Texts(models.Model):
    """
    Model of reminders
    """
    levels_to_select =[
        ('Friendly reminder','Friendly reminder' ),
        ('Your invoice is overdue', 'Your invoice is overdue'),
        ('Your invoice is overdue II', 'Your invoice is overdue II'),
        ('Urgent overdue invoice', 'Urgent overdue invoice'),
    ]

    owner =  models.ForeignKey(User, on_delete=models.CASCADE)
    levels = models.CharField(max_length=100,  choices=levels_to_select, unique=True)
    text = models.TextField()

    def __str__(self):
        return self.levels
