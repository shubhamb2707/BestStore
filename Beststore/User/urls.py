from django.contrib import admin
from django.urls import path
from User import views

urlpatterns = [
    path('register/',views.register,name="register"),
    path('login/',views.Login_View,name="login"),
    path('logout/',views.Logout_View,name="logout"),
    path('index/', views.index, name="index"),

]
