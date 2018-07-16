from django.urls import path

from . import views


urlpatterns = [
    path('', views.work, name='home'),
    path('contact', views.contact, name='contact'),
    path('success/', views.successView, name='success'),
]

