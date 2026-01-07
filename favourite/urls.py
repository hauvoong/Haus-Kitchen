from . import views
from django.urls import path

urlpatterns = [
    path('', views.favourite_recipes, name='favourite'),
]