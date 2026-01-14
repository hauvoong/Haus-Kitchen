from django.db import models
from django.contrib.auth.models import User
from recipes.models import Recipe

class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favourites')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='favourited_by')
    notes = models.TextField(blank=True, null=True)
    added_at = models.DateTimeField(auto_now_add=True)
    paginate_by = 3

    class Meta:
        unique_together = ('user', 'recipe')

    def __str__(self):
        return f"{self.recipe.title} recipe has been favourited by {self.user}"