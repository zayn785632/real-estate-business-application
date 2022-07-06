from django.urls import URLPattern, path

from . import views

urlpatterns = [
    path('contact', views.contact, name='contact')
]