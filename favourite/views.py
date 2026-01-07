from django.shortcuts import render
from favourite.models import Favourite

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

  