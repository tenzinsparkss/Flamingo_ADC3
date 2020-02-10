from django.urls import path
from . import views
from .views import update_recipe, recipe_list

app_name= 'main'
urlpatterns = [
    path('', views.home, name="Homepage"),
    path('register/', views.register, name= 'register'),
    path('index/', views.home, name='Homepage'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('uploaded/', views.recipe_list, name="recipe_list"),
    path('recipe/upload/', views.upload_recipe, name='upload'),
    path('additems/', views.add_items, name = 'additems'),
    path('blog/', views.blog, name = 'blog'),
    path('uploaded/<int:pk>/', views.delete_recipe, name='delete_recipe'),
    # path('uploaded/update_recipe/<int:item_id>/', views.update_recipe, name='update_recipe'),
    path('uploaded/update_recipe/<int:id>/', update_recipe.as_view(), name='update_recipe'),
    path('recipe_list/', views.recipe_list, name='recipe_list'),

]
