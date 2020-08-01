from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Stats(models.Model):
    total_cases = models.CharField(max_length=264)
    deaths = models.CharField(max_length=264)
    recovered_cases = models.CharField(max_length=264)
    new_date = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.total_cases

class News(models.Model):
    headline = models.CharField(max_length=264)
    link = models.URLField(max_length=200)
    cur_date = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.cur_date)

class Leacher(models.Model):
    name = models.CharField(max_length=264)
    address = models.CharField(max_length=1032)
    location = models.CharField(max_length=264)

    def __str__(self):
        return str(self.name)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.location

#modified code

class Donation(models.Model):
    donator = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True)
    #receiver = models.ForeignKey(Leacher, on_delete=models.CASCADE)
    item = models.CharField(max_length=264)
    amount = models.CharField(max_length=264)

    def __str__(self):
        return self.item
#

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


