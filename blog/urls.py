from django.urls import path
from . import views

urlpatterns = [
    path('', views.daftar_post, name='daftar_post'),
    path('post/<int:pk>/', views.detail_post, name='detail_post'),
    path('post/baru/', views.baru_post, name='baru_post'),
    path('post/<int:pk>/edit/', views.edit_post, name='edit_post'),
]