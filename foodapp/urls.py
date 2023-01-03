from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("menu", views.menu, name="menu"),
    path("hotels", views.hotels, name="hotels"),
    path("register", views.register, name="register"),
    path("login", views.login_user, name="login"),
    path("logout", views.logout_request, name= "logout"),
]