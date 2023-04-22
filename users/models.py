from django.db import models
import uuid
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    username = models.CharField(max_length=15, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    short_intro = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/', default='profiles/user-default.png')
    social_facebook = models.CharField(max_length=50, blank=True, null=True)
    social_twitter = models.CharField(max_length=50, blank=True, null=True)
    social_instagram = models.CharField(max_length=50, blank=True, null=True)
    social_youtube = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.user.username)


class Skill(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    skill = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.skill
