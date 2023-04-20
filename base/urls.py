from django.urls import path
from . import views
urlpatterns = [
    path('', views.properties, name="properties"),
    path('property/<str:pk>/', views.property, name="property"),

    path('create-property', views.create_property, name="create-property"),
    path('update-property/<str:pk>/', views.update_property, name="update-property"),
    path('delete-property/<str:pk>/', views.delete_property, name="delete-property"),

]
