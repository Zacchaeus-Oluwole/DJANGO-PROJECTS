from django.urls import path
from . import views


urlpatterns = [
    # post views
    # path('login/', views.user_login, name='login'),
    # path('reg', views.register, name='/'),
    path('', views.perpe, name='/'),
    path('show', views.show, name='/'),
    path('edit', views.edit, name='/'),
    path('search/', views.search_offence)
]