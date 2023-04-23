from django.urls import path
from . import views
urlpatterns = [
    path('profiles/', views.profiles_page, name="profiles"),
    path('profile/<str:pk>/', views.user_profile_page, name="profile"),

    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_page, name="logout"),
    path('register/', views.register_page, name="register"),
]