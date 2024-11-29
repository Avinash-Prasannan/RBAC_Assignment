from django.urls import path
from Demo import views

urlpatterns = [
    path('register', views.register),
    path('', views.login),
    path('home', views.admin_home),
    path('moderator/home',views.moderator_home),
    path('user/home', views.user_home),
]
