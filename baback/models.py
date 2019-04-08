from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.

class Lab(models.Model):
    lab_name = models.CharField(max_length = 200)
    lab_country = models.CharField(max_length = 200)
    lab_method = models.CharField(max_length = 200)
    lab_date = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.lab_name

class Color(models.Model):
    base_color = models.CharField(max_length = 200)
    white_color = models.CharField(max_length = 200, blank=True)
    marks = models.CharField(max_length = 200, blank=True)
    def __str__(self):
       return self.base_color

class Genotype(models.Model):
    SILVER = ((u'Zz', u'Zz'),(u'ZZ', u'ZZ'), (u'zz', u'zz'), (u'N/N', u'N/N'))
    CREMELLO = ((u'CcrCcr', u'CcrCcr'), (u'Ccr/ccr', u'Ccr/ccr'), (u'ccr/ccr', u'ccr/ccr'), (u'N/N', u'N/N'))
    DUN = ((u'Dd', u'Dd'),(u'DD', u'DD'), (u'dd', u'dd'), (u'N/N', u'N/N'))
    CHAMPAGNE = ((u'Chch', u'Chch'),(u'CHCH', u'CHCH'), (u'chch', u'chch'), (u'N/N', u'N/N'))
    description = models.CharField(max_length=200, default = 'N/N')
    base_formula = models.CharField(max_length = 200)
    silver = models.CharField(choices = SILVER, max_length = 10, default = 'N/N')
    cream = models.CharField(choices = CREMELLO, max_length = 10, default = 'N/N')
    dun = models.CharField(choices = DUN, max_length = 10, default = 'N/N')
    champagne = models.CharField(choices = CHAMPAGNE, max_length = 10, default = 'N/N')
    disease = models.CharField(max_length = 200, blank=True)
    lab = models.ForeignKey(Lab, default = 1, on_delete = models.SET_DEFAULT)
    color = models.ForeignKey(Color, default = 1, on_delete = models.SET_DEFAULT)
    def __str__(self):
       return self.description


class Owner(models.Model):
    name = models.CharField(max_length = 200)
    phone = models.CharField(max_length = 50)
    address = models.CharField(max_length = 200, blank=True)
    farm = models.CharField(max_length = 200, blank=True)
    country = models.CharField(max_length = 50, blank=True)
    email = models.EmailField(max_length = 50, default = 'Nope@heckno.ru')

    def __str__(self):
       return self.name

class Horse(models.Model):
    GENDER = ((u'Ж', u'Жеребец'), (u'К', u'Кобыла'), (u'М', u'Мерин'))
    horse_name = models.CharField(max_length = 200)
    sex = models.CharField(max_length = 1, choices = GENDER)
    birth_date = models.IntegerField()
    death_date = models.IntegerField(blank=True, null=True)
    breed = models.CharField(max_length = 100)
    photo = models.ImageField(upload_to='images', height_field=None, width_field=None, max_length=100, default = 'images/base.jpg')
    horse_color = models.ForeignKey(Color)
    genes = models.ForeignKey(Genotype, default = 1, on_delete = models.SET_DEFAULT)
    owner = models.ForeignKey(Owner, default = 1, on_delete = models.SET_DEFAULT)
    def __str__(self):
       return self.horse_name

# class CustomUser(AbstractUser):
#     admin = models.BooleanField()
#     own = models.BooleanField()
#     usr = models.BooleanField()

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    admin = models.BooleanField()
    own = models.BooleanField()
    usr = models.BooleanField()
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        CustomUser.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.customuser.save()
