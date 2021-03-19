from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Clients(models.Model):
    PAYEMENTS = [
    ('30', '30 days'),
    ('END', 'End of the current month'),
]
    actif = models.BooleanField(null=True, default=True)
    number =  models.CharField(max_length=50, null=True)
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE)
    companyName = models.CharField(max_length=50)
    name = models.CharField(max_length=50)#must be converted to a choices field
    firstName = models.CharField(max_length=100)
    adress = models.CharField(max_length=50)#must be converted to a choices field(algo of countries)
    countrie = models.CharField(max_length=50)#must be converted to a choices field
    city = models.CharField(max_length=50)#must be converted to a choices field
    postCode = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    taxNum = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    website = models.CharField(max_length=50, blank=True)
    comment = models.TextField(max_length=50, blank=True, null=True)
    payments_conditions = models.CharField(max_length=10,choices=PAYEMENTS,null=True)

    def __str__(self):
        return self.name
