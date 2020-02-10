from django.test import TestCase
from .models import Recipe

# Create your tests here.
class RecipeTestCase:
    def setUp(self):
        Recipe.objects.create(recipe_title="tsampa", recipe_category="wheat")
        Recipe.objects.create(reciep_title="yaksha", recipe_category="meat")

    def test_recipe(self):
        tsampa = Recipe.objects.get(recipe_title="tsampa")
        yaksha = Recipe.objects.get(recipe_title="yaksha")
        self.assertEqual(tsampa.food(), 'This tsampa made of "wheat"')
        self.assertEqual(yaksha.food(), 'This yaksha made of "meat"')


