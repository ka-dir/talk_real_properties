from django.forms import ModelForm
from .models import Property
from django import forms


class PropertyForm(ModelForm):
    class Meta:
        model = Property
        fields = [
            'title', 'description', 'featured_image', 'property_type', 'price', 'location',
            'property_status', 'tags',
        ]
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __int__(self, *args, **kwargs):
        super(PropertyForm, self).__init__(*args, **kwargs)
        # self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': "Enter Title"})
        for k, v in self.fields.items():
            v.widget.attrs.update({'class': 'form-control'})
