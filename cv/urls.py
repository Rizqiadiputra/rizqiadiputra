from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about.html', views.about, name='about'),
    path('services.html',views.services, name='service'),
    path('portfolio.html', views.portfolio, name='portfolio'),
    path('blog.html', views.blog, name='blog'),
]