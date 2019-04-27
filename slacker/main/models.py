from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	img = models.ImageField(upload_to='media/images/',default='/media/images/765-default-avatar.png', null=True, blank=True)
	bio = models.TextField(max_length=500, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()

class PrivateChat(models.Model):
	profiles = models.ManyToManyField(Profile)

class GroupChat(models.Model):
	name = models.CharField(max_length=50)
	profiles = models.ManyToManyField(Profile)


class Message(models.Model):
	content = models.TextField(max_length=500, blank=True)
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
	timestamp = models.DateTimeField(default=timezone.now)

class GroupMessage(Message):
	chat = models.ForeignKey(GroupChat, on_delete=models.CASCADE)

class PrivateMessage(Message):
	chat = models.ForeignKey(PrivateChat, on_delete=models.CASCADE)



