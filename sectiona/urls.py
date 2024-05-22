# sectiona/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('genders', views.index_gender, name='index_gender'),
    path('gender/create', views.create_gender, name='create_gender'),
    path('gender_store', views.store_gender),
]
