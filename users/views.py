from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def profiles_page(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)


def user_profile_page(request, pk):
    profile = Profile.objects.get(id=pk)
    top_skill = profile.skill_set.exclude(description__exact='')  # exclude if skill does not have description
    other_skill = profile.skill_set.filter(description="")
    context = {'profile': profile, 'top_skill': top_skill, 'other_skill': other_skill}
    return render(request, 'users/user-profile.html', context)


# login

def login_page(request):
    if request.user.is_authenticated:
        return redirect('properties')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "username does not exist")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('properties')
        else:
            messages.error(request, "Username OR Password is incorrect")

    context = {}
    return render(request, 'users/login.html', context)


#  logout
def logout_page(request):
    logout(request)
    messages.info(request, "You logged out successfully")
    return redirect('login')


#  register
def register_page(request):
    forms = UserCreationForm()
    if request.method == 'POST':
        forms = UserCreationForm(request.POST)
        if forms.is_valid():
            user = forms.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'User account created successfully')
            return redirect('properties')
    context = {'forms': forms}
    return render(request, 'users/register.html', context)
