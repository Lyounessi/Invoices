from django.db import models
from django.contrib.auth.models import User
from clients.models import Clients
from stocks.models import Article
############################ In logics imports ##############################
from datetime import date



class Invoices(models.Model):
    """
    Model of Invoices
    """
    stats_to_select =[
        ('payed','pyd' ),
        ('notPayed', 'npyd'),
        ('canceled', 'cnl'),
        
    ]
    back_stats =[
        ('finished', 'fnsh'),
        ('insave', 'insv'),
    ]
    title = models.CharField(max_length=150, blank=True, null=True)
    logo = models.ImageField(blank=True)
    dateCreation = models.DateField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    artice = models.ManyToManyField(Article)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    stats = models.CharField(max_length=100,  choices=stats_to_select, default='notPayed')
    prov_numb = models.CharField(max_length=150, blank=True, null=True)
    number = models.CharField(max_length=150, blank=True, null=True)
    fnb = models.CharField(max_length=150, blank=True, null=True)
    back_status = models.CharField(max_length=100,  choices=back_stats, blank=True, null=True)
     
    
    
    
    def __str__(self):
        return self.stats

   


class Quotes(models.Model):
    """
    Model of quotes
    """
    stats_to_select =[
        ('rej', 'rejected'),
        ('inw', 'in wait'),
        ('acc', 'accepted'),
        
    ]
    title = models.CharField(max_length=150, blank=True, null=True)
    logo = models.ImageField(blank=True)
    dateCreation = models.DateField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    artice = models.ManyToManyField(Article)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    stats = models.CharField(max_length=100,  choices=stats_to_select, default='inw')
    number = models.CharField(max_length=150, unique=True)
     
    
    
    
    def __str__(self):
        return self.stats