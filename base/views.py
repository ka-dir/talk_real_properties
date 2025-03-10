from django.shortcuts import render, redirect
from .models import Property
from .forms import PropertyForm
from django.contrib.auth.decorators import login_required



# Create your views here.

def properties(request):
    properties = Property.objects.all()
    context = {'properties': properties}
    return render(request, 'base/properties.html', context)


def property(request, pk):
    property = Property.objects.get(id=pk)
    context = {'property': property}
    return render(request, 'base/property.html', context)


# add new property
@login_required(login_url='login')
def create_property(request):
    property_form = PropertyForm()
    if request.method == 'POST':
        # print(request.POST)
        property_form = PropertyForm(request.POST, request.FILES)
        if property_form.is_valid():
            property_form.save()
            return redirect('properties')
    context = {'property_form': property_form}
    return render(request, 'base/property-form.html', context)


# edit property
@login_required(login_url='login')
def update_property(request, pk):
    property = Property.objects.get(id=pk)
    property_form = PropertyForm(instance=property)
    if request.method == 'POST':
        property_form = PropertyForm(request.POST, request.FILES, instance=property)
        if property_form.is_valid():
            property_form.save()
            return redirect('properties')
    context = {'property_form': property_form}
    return render(request, 'base/property-form.html', context)


# delete property
@login_required(login_url='login')
def delete_property(request, pk):
    project_obj = Property.objects.get(id=pk)
    if request.method == 'POST':
        project_obj.delete()
        return redirect('properties')
    context = {'obj': project_obj}
    return render(request, 'base/delete-template.html', context)
