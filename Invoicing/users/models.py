from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    # must be converted to a choices field
    activityDom = models.CharField(max_length=50)
    adress = models.TextField()
    # must be converted to a choices field
    countrie = models.CharField(max_length=50)
    # must be converted to a choices field(algo of countries)
    city = models.CharField(max_length=50)
    postCode = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    taxNum = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    logo = models.ImageField(blank=True)

    def __str__(self):
        return self.name
