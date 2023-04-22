from django.urls import path
from . import views
urlpatterns = [
    path('profiles/', views.profiles_page, name="profiles"),
]