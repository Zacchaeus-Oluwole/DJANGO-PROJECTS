from django.urls import path
from . import views

urlpatterns = [
    path('', views.perpe, name='/'),
    path('result/', views.result),
    path('search/', views.search_offence)
]