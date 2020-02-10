from django.shortcuts import render, redirect
from main.models import Recipe
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

# To get all data from db
def api_data(request):
    recipe = Recipe.objects.all()
    if request.method == "GET":
        dictionary_type = {"recipes": list(recipe.values("recipe_title", "recipe_category"))}

        return JsonResponse(dictionary_type)

# To fetch a specific data of recipe from db
@csrf_exempt
def update_api_data(request, pk):
    recipe = Recipe.objects.get(pk = pk)
    if request.method == "GET":
        print("Testing")
        return JsonResponse({"recipe_title": recipe.recipe_title, "reciple_category": recipe.recipe_category})
    elif request.method == "PUT":
        json_data = request.body.decode('utf-8')
        update_data = json.loads(json_data)
        recipe.recipe_title = update_data['recipe_title']
        recipe.recipe_category = update_data['recipe_category']
        recipe.save()
        return JsonResponse({"message": "Successfully completed!!"})
    elif request.method == "DELETE":
        recipe.delete()
        return JsonResponse({"message": "Successfully!"})


# Pagination by filtering a page and size as per request.
def api_recipe(request, PAGENO, SIZE):
    if request.method == "GET":
        skip = SIZE * (PAGENO -1)
        recipe = Recipe.objects.all() [skip:(PAGENO * SIZE)]
        dictionary_type = {"recipe":list(recipe.values( "date_time", "id", "item", "item_id", "recipe_category", "recipe_description", "recipe_favorites", "recipe_image", "recipe_title"))}
    return JsonResponse(dictionary_type)    


# To modify or remove a data from Recipe Model from database
@csrf_exempt
def api_add_recipe(request):
    if request.method == "POST":
        json_data = request.body.decode('utf-8')
        add_recipe = json.loads(json_data)

        recipe_title = add_recipe['recipe_title']
        recipe_description = add_recipe['recipe_description']
        recipe_category = add_recipe['recipe_category']
        recipe = Recipe.objects.create(recipe_title=recipe_title, recipe_description = recipe_description, recipe_category = recipe_category)
        try:
            recipe.save()
            
            return JsonResponse({"Created!":"Recipe has been added successfully..."})
        
        except:
            
            return JsonResponse({"Error!":"Recipe could not be created..."})