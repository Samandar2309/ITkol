from django.urls import path
from .views import index, services, contact, about, cases

urlpatterns = [
    path('', index, name='index'),
    path('services.html', services, name='services'),
    path('contact.html', contact, name='contact'),
    path('about.html', about, name='about'),
    path('case_study.html', cases, name='cases'),

]
