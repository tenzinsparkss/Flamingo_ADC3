from django.test import TestCase
from .models import Recipe, Comment, User, Item

# Create your tests here.

# Recipe model Test Case
class RecipeTest(TestCase):
    def setUp(self):
        Recipe.objects.create(recipe_title="tsampa", recipe_category="wheat")
        Recipe.objects.create(reciep_title="yaksha", recipe_category="meat")

    def test_recipe(self):
        tsampa = Recipe.objects.get(recipe_title="tsampa")
        yaksha = Recipe.objects.get(recipe_title="yaksha")
        self.assertEqual(tsampa.food(), 'This tsampa made of "wheat"')
        self.assertEqual(yaksha.food(), 'This yaksha made of "meat"')

# Comment model Test Case
class CommentTest(TestCase):
    def setUp(self):
        u_obj = User.objects.create(username = "Tenzin", email = "tenzin@gmail.com")
        # i_obj = Item.objects.create(item_title = "Momos")
        c_obj = Comment.objects.create(msg = "beautiful", commented_by = u_obj, item = i_obj)

    def test_comment(self):
        user = User.objects.get(username = "Tenzin")
        comment = Comment.objects.get(msg= "beautiful")
        self.assertEqual(user.username, "Tenzin")
        self.assertEqual(comment.msg, "beautiful")

