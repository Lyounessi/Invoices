from django.db import models
from django.contrib.auth.models import User





class Units(models.Model):
    

    name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name

   

class Article(models.Model):

    types_to_select =[
        ('srv', 'service'),
        ('prod', 'product'),
    ]


    
    owner =  models.ForeignKey(User, on_delete=models.CASCADE)
    articleType = models.CharField(max_length=100,  choices=types_to_select)
    name = models.CharField(max_length=150, blank=True)
    ref = models.CharField(max_length=150, blank=True)
    unit = models.ForeignKey(Units, on_delete=models.CASCADE)
    tax = models.IntegerField(blank=True)
    actif = models.BooleanField(null=True, default=True)
    buyPrice = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    gainMargin = models.DecimalField(max_digits=19, decimal_places=2,  blank=True,null=True)
    sellPrice = models.DecimalField(max_digits=19, decimal_places=2,  blank=True,null=True)

    def __str__(self):
        return '{} {}'.format(self.name, self.articleType)

    