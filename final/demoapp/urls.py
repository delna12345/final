from django.urls import path
from . import views

urlpatterns = [
    path('',views.demo,name='demo'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('submit_form',views.submit_form,name='submit_form'),
    path('logout',views.logout,name='logout'),
]