from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(accounts=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

# @receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
# def save_profile(sender, instance, created, **kwargs):
#     user = instance
#     if created:
#         profile = Profile(user=user)
#         profile.save()