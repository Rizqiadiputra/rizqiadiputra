from django.urls import path
from . import views

urlpatterns = [
    path('', views.daftar_post, name='daftar_post'),
]