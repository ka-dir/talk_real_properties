import uuid

from django.db import models


# Create your models here.

class Property(models.Model):
    PROPERTY_STATUS = (
        ('AVAILABLE', 'AVAILABLE'),
        ('BOOKED', 'BOOKED'),
    )
    property_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.IntegerField(default=0, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    property_status = models.CharField(max_length=100, choices=PROPERTY_STATUS, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)

    def __str__(self):
        return self.property_name
