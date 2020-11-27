from django.db import models
from django.contrib.auth.models import User
from clients.models import Clients



class Invoices(models.Model):
    stats_to_select =[
        ('pyd', 'payed'),
        ('npyd', 'notPayed'),
        ('cnl', 'canceled'),
        
    ]
    title = models.CharField(max_length=150, blank=True, null=True)
    logo = models.ImageField(blank=True)
    dateCreation = models.DateField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    #artice = To add as an FK
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    stats = models.CharField(max_length=100,  choices=stats_to_select, default='npyd')
    number = models.CharField(max_length=150, unique=True)
     
    
    
    
    def __str__(self):
        return self.number

   