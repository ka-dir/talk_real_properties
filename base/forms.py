from django.forms import ModelForm
from .models import Property


class PropertyForm(ModelForm):
    class Meta:
        model = Property
        fields = [
            'title', 'description', 'featured_image', 'property_type', 'price', 'location',
            'property_status', 'tags'
        ]
