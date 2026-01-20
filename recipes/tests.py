from django.test import TestCase
from .models import Recipe  # Adjust import if your model is named differently


class RecipeModelTest(TestCase):
    def test_create_recipe(self):
        recipe = Recipe.objects.create(
            title="Test Recipe",
            content="A simple test recipe.",
            # Add other required fields here
        )
        self.assertEqual(recipe.title, "Test Recipe")
        # If you have __str__ defined
        self.assertEqual(str(recipe), "Test Recipe")
