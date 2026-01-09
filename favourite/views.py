from django.shortcuts import render, redirect, get_object_or_404
from favourite.models import Favourite
from recipes.models import Recipe
from django.contrib.auth.decorators import login_required
from .models import Favourite
from django.contrib import messages

# Create your views here.
def favourite_recipes(request):
    """
    Renders the user's favourite recipes page but must be logged in. 
    It uses if not to check user authentication.
    Filter retrieves all favourited recipes by user in one query.
    """
    if not request.user.is_authenticated:
        return render(request, "registration/login.html", {"error": "You must be logged in to add recipes to your favourites."})
    user = request.user
    favourites = Favourite.objects.filter(user=user).select_related('recipe')

    return render(
        request,
        "favourite/favourite.html",
        {"favourites": favourites},
    )

@login_required
def add_to_favourites(request, recipe_id):
    if request.method == "POST":
        recipe = get_object_or_404(Recipe, id=recipe_id)
        Favourite.objects.get_or_create(user=request.user, recipe=recipe)
        messages.success(request, f'"{recipe.title}" has been added to your favourites.')

    return redirect(request.META.get('HTTP_REFERER', 'recipes:index'))  # Redirects back to previous page


def favourites_list(request):
    favourites = Favourite.objects.filter(user=request.user)
    return render(request, 'favourite/favourites.html', {'favourites': favourites})

@login_required
def remove_favourite(request, fav_id):
    """Remove a recipe from user's favourites"""
    favourite = get_object_or_404(Favourite, id=fav_id, user=request.user)
    recipe_title = favourite.recipe.title
    favourite.delete()
    messages.success(request, f'"{recipe_title}" has been removed from your favourites.')
    return redirect('favourite')
