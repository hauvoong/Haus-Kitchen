from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Recipe
from .forms import CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .forms import RecipeForm




# Create your views here.
class RecipeList(generic.ListView):
    queryset = Recipe.objects.all()
    template_name = "recipes/index.html"
    paginate_by = 4


def recipe_detail(request, slug):
    """
    Display an individual :model:`recipes.Recipe`.

    **Context**

    ``recipe``
        An instance of :model:`recipes.Recipe`.

    **Template:**

    :template:`recipes/recipe_detail.html`
    """

    queryset = Recipe.objects.all()
    recipe = get_object_or_404(queryset, slug=slug)

    comments = recipe.comments.all().order_by("-created_at")
    comment_count = recipe.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.recipe = recipe
            comment.save()
            messages.add_message(
        request, messages.SUCCESS,
        'Comment submitted and awaiting approval'
    )

    comment_form = CommentForm()

    return render(
        request,
        "recipes/recipe_detail.html",
        {
            "recipe": recipe,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
)


@login_required
def add_recipe(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index.html')  # Change to your recipe list view name
    else:
        form = RecipeForm()
    return render(request, 'recipes/add_recipe.html', {'form': form})