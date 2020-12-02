from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('unlogindex/', views.unlogindex, name='unlogin'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('index/', views.index),
    path('logout/',views.logout,name='logout'),
    path('renew/',views.renew,name='renew'),
    path('add/',views.add,name='add'),
]
