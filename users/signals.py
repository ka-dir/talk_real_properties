from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


#  @receiver(post_save, sender=Profile)
def create_profile(sender, instance, created, **kwargs):
    # print("profile updated!!")
    # print("instance:", instance)
    # print("created:", created)
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.username,
        )


def delete_user(sender, instance, **kwargs):
    # print("deleting user ...")
    user = instance.user
    user.delete()


post_save.connect(create_profile, sender=User)
post_delete.connect(delete_user, sender=Profile)
