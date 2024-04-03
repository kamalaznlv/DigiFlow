from django.urls import path
from . import views

urlpatterns = [
    path('landingpage/', views.landingpage, name='landingpage'),
]