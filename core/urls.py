from django.contrib import admin
from django.urls import path
from .views import home,processar_csv

urlpatterns = [
    path('', home, name="home"),
    path('processar_csv/', processar_csv, name='processar_csv'),
]