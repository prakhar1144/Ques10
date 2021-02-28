from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Award(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    points = models.IntegerField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class User_Detail(models.Model):
    user = models.OneToOneField(User, on_delete=models.RESTRICT)
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=50, help_text="Enter your city and state name", blank=True)
    picture = models.ImageField(null=True, blank=True) 
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    award1 = models.ForeignKey(Award, on_delete=models.RESTRICT, related_name="award1", blank=True, null=True)
    award2 = models.ForeignKey(Award, on_delete=models.RESTRICT, related_name="award2", blank=True, null=True)
    award3 = models.ForeignKey(Award, on_delete=models.RESTRICT, related_name="award3", blank=True, null=True)
    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def create_user_detail(sender, instance, created, **kwargs):
    if created:
        User_Detail.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_detail(sender, instance, **kwargs):
    instance.user_detail.save()



