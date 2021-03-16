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
        ('Finilised', 'fnsh'),
        ('In save', 'insv'),
        ('In Process', 'inpro'),

    ]
    title = models.CharField(max_length=150, blank=True, null=True)
    logo = models.ImageField(blank=True)
    dateCreation = models.DateField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE, blank=True, null=True)
    stats = models.CharField(max_length=100,  choices=stats_to_select, default='notPayed')
    prov_numb = models.CharField(max_length=150, blank=True, null=True)# When invoice is not finished
    number = models.CharField(max_length=150, blank=True, null=True)# when invoice is finished
    fnb = models.CharField(max_length=150, blank=True, null=True)
    back_status = models.CharField(max_length=100,  choices=back_stats, blank=True, null=True)
     
    def __str__(self):
        return str(self.pk)

   
class Article_Inv(models.Model):
    """
    Many to many trough article in invoices
    """
    invoice = models.ForeignKey(Invoices, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    tax_one =  models.IntegerField(blank=True, null=True, default=0)
    tax_two = models.IntegerField(blank=True, null=True, default=0) 
    remise = models.IntegerField(blank=True, null=True, default=0) 
    qte = models.IntegerField(blank=True, null=True, default=1) 
    amount = models.CharField(max_length=50, null=True,)
    
    
    def __str__(self):
        return str(self.pk)
    
    class Meta:
        unique_together = [['invoice','article']]
       
   





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