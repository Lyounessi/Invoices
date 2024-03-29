from django.db import models
from django.contrib.auth.models import User
from clients.models import Clients
from stocks.models import Article
############################ In logics imports ##############################
from datetime import date
from django.db.models.signals import post_delete, post_save, pre_save
from django.dispatch import receiver

class PaymentsMethods(models.Model):
    """
    Model of payment method
    """
   
    method = models.CharField(max_length=150, unique=True, blank=True, null=True)
    

    def __str__(self):
        return str(self.method)


class Invoices(models.Model):
    """
    Model of Invoices
    """
    stats_to_select =[
        ('payed','pyd' ),
        ('unpaied', 'npyd'),
        ('canceled', 'cnl'),
        ('partial payed', 'part-payed'),
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
    stats = models.CharField(max_length=100,  choices=stats_to_select, default='unpaid')
    payment_method =  models.ForeignKey(PaymentsMethods, on_delete=models.CASCADE, blank=True, null=True)
    prov_numb = models.CharField(max_length=150, blank=True, null=True)# When invoice is not finished
    number = models.CharField(max_length=150, blank=True, null=True)# when invoice is finished
    fnb = models.CharField(max_length=150, blank=True, null=True)
    back_status = models.CharField(max_length=100,  choices=back_stats, blank=True, null=True)
    sent = models.BooleanField(default=False)
    deadlinePay = models.CharField(max_length=100,  blank=True, null=True) 
    still_to_pay = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True, default=0)
    sub_total = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True, default=0)
    tax_one = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True, default=0)
    tax_two = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True, default=0)
    total = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True, default=0)

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
        ('rejected', 'rejected'),
        ('in wait', 'in wait'),
        ('accepted', 'accepted'),
        
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
    stats = models.CharField(max_length=100,  choices=stats_to_select, default='in wait')
    payment_method =  models.ForeignKey(PaymentsMethods, on_delete=models.CASCADE, blank=True, null=True)
    prov_numb = models.CharField(max_length=150, blank=True, null=True)# When invoice is not finished
    number = models.CharField(max_length=150, blank=True, null=True)# when invoice is finished
    fnb = models.CharField(max_length=150, blank=True, null=True)
    back_status = models.CharField(max_length=100,  choices=back_stats, blank=True, null=True)
    sent = models.BooleanField(default=False)
    sub_total = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True, default=0)
    tax_one = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True, default=0)
    tax_two = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True, default=0)
    total = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True, default=0)

    def __str__(self):
        return str(self.pk)
     
    
    
    
    def __str__(self):
        return self.stats



class Article_Quotes(models.Model):
    """
    Many to many trough article in quotes
    """
    quote = models.ForeignKey(Quotes, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    tax_one =  models.IntegerField(blank=True, null=True, default=0)
    tax_two = models.IntegerField(blank=True, null=True, default=0) 
    remise = models.IntegerField(blank=True, null=True, default=0) 
    qte = models.IntegerField(blank=True, null=True, default=1) 
    amount = models.CharField(max_length=50, null=True,)
    

    def __str__(self):
        return str(self.pk)
    
    class Meta:
        unique_together = [['quote','article']]
       
   