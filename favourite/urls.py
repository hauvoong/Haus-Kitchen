from . import views
from django.urls import path

urlpatterns = [
    path('', views.favourite_recipes, name='favourite'),
    path('add/<int:recipe_id>/', views.add_to_favourites, name='add_to_favourites'),
    path('my-favourites/', views.favourites_list, name='favourites_list'),
    path('favourite/remove/<int:fav_id>/', views.remove_favourite, name='remove_favourite'),
]