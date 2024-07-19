
from django.urls import path

from app2 import views

urlpatterns = [
    path('',views.index,name='home'),
    path('about',views.about,name='about'),
    path('services',views.services,name='services'),
    path('contact',views.contact,name='contact'),
    path('admin',views.admin,name='admin'),
    path('signup',views.signup,name='signup'),
]
