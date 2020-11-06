from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=50)
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
"""
class Logo(models.Model):
    
    logo = models.CharField(_(""), max_length=50)

    class Meta:
        verbose_name = _("")
        verbose_name_plural = _("s")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
"""

class Company(models.Model):
    
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    activityDom = models.CharField(max_length=50)#must be converted to a choices field
    adress = models.CharField(max_length=100)
    countrie = models.CharField(max_length=50)#must be converted to a choices field
    city = models.CharField(max_length=50)#must be converted to a choices field(algo of countries)
    postCode = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    taxNum = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    logo = models.CharField( max_length=50)


    def __str__(self):
        return self.name
