import uuid

from django.db import models
from users.models import Profile

# Create your models here.

class Property(models.Model):
    PROPERTY_STATUS = (
        ('AVAILABLE', 'AVAILABLE'),
        ('BOOKED', 'BOOKED'),
    )
    owner = models.ForeignKey(Profile, blank=True, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=100)
    description = models.TextField()
    featured_image = models.ImageField(null=True, blank=True, default="default.png")
    property_type = models.ForeignKey('PropertyType', on_delete=models.SET_NULL, blank=True, null=True)
    price = models.IntegerField(default=0, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    property_status = models.CharField(max_length=100, choices=PROPERTY_STATUS, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True, null=True)
    vote_total = models.IntegerField(default=0, blank=True, null=True)
    vote_ratio = models.IntegerField(default=0, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'


class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )
    #  owner
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    review = models.TextField(max_length=255, blank=True, null=True)
    vote = models.CharField(max_length=50, blank=True, null=True, choices=VOTE_TYPE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.vote


class Tag(models.Model):
    hashtags = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.hashtags


class PropertyType(models.Model):
    PROPERTY_TYPE = (
        ('Land', 'Land'),
        ('Residential', 'Residential'),
        ('Commercial', 'Commercial'),
        ('Industrial', 'Industrial'),
    )
    category = models.CharField(max_length=100, blank=True, null=True, choices=PROPERTY_TYPE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = "PropertyType"
        verbose_name_plural = "PropertyTypes"
