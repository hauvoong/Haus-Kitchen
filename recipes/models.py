from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    #image_url = CloudinaryField('image', default='placeholder')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commenter')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Comment from {self.author} on {self.recipe.title} recipe"
    

class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favourites')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='favourited_by')
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'recipe')

    def __str__(self):
        return f"{self.recipe.title} recipe has been favourited by {self.user}"
    

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ratings')
    score = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    rated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'recipe')

    def __str__(self):
        return f"{self.user} rated {self.recipe.title} as {self.score}/5"