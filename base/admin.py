from django.contrib import admin
from . models import Property, Review, Tag, PropertyType
# Register your models here.

admin.site.register(Property)
admin.site.register(Review)
admin.site.register(Tag)
admin.site.register(PropertyType)