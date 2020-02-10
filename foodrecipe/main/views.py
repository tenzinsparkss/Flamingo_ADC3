from django.shortcuts import render, redirect
from django.http import HttpResponse,request
from .forms import RegistrationForm, RecipeForm, ItemForm
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from django.views import View, generic
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from .models import Recipe, Comment, Item, User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from django.views.generic import ListView
from django.contrib import messages
from django.http import JsonResponse
from .decorators import authenticated_user, admin_only


# Create your views here...
def home(request):
    recipe = Recipe.objects.all()
    return render(request,'main/index.html',{'recipes':recipe})

# Comment section is here..
def blog(request):
    containe = []
    if request.method == "POST":
        t=request.POST["tenzin"]
        print("Testing", Item.objects.get(id=t))
        print("User ID is ", request.user.id)
        obj_item=Comment(msg = request.POST['msg'],
        commented_by = User.objects.get(id=request.user.id),item=Item.objects.get(id=t))
        obj_item.save()
        recipe = Recipe.objects.all()
        return redirect('main:blog')
    
    else:
        blog = Item.objects.all()
        print("Testing",blog)
        for i in blog:
            containe.append(Comment.objects.filter(item=i))

    return render(request, 'main/blog.html',{'blog':blog, 'containe': containe})        
    

# Adding an item 
@login_required(login_url='/login/')
def add_items(request):
    # additems=12123
    form = ItemForm()
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            if request.user:
                form.save()
            else:
                return render(request, "main/adding_items.html")
            return redirect('main:additems')
    return render(request, "main/adding_items.html", {"form":form})


# User registration is here
@authenticated_user
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
           user = form.save()
           email = form.cleaned_data.get('email')
           password =form.cleaned_data.get('password1')
           print("email is",password)
           userr =auth.authenticate(email = email, password = password)
           auth.login(request, userr)
       
           return redirect('main:Homepage')
        else:
            print("Error while registration")
    else:
        form = RegistrationForm()
    return render(request ,'main/register.html', {'form': form})   


# User login is here
def Login(request):
    if request.method == "POST":
        form = AuthenticationForm(request = request, data = request.POST)
        print("form data is", form)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print('user is ',user)
            if user is not None:

                login(request, user)
                return redirect('main:blog')
                messages.success(request, f'you have logged as {{ username }}')
                
            else:
                pass
        else:
            print("Testing")
    form = AuthenticationForm()
    return render(request, "main/login.html", context = {"form" : form})

   
# User logout
def Logout(request):
    logout(request)
    return redirect('main:Homepage') 


# upload here for Recipe
@login_required(login_url='/login/')
def upload_recipe(request):
    form = RecipeForm()
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            if request.user:
                form.save()
            else:
                messages.success(request, f'Please enter a correct email and password...')
                return render(request, "main/login.html")
            return redirect('main:recipe_list')
    return render(request, "main/upload_recipe.html", {"form":form})


# Recipe_list creates object of Model (Recipe)
@login_required(login_url='/login/')
# @authenticated_user
def recipe_list(request):
    recipe =  Recipe.objects.all()
    print("asdsad", recipe)
    if request.GET:
        query = request.GET['q']
        recipe = get_data_queryset(str(query))
    return render(request, "main/recipe_list.html", {"recipes":recipe})



# Update_recipe is class based views
class update_recipe(View):
    template_name = 'main/update.html'
    def get_object(self): 
        obj = None
        id = self.kwargs.get('id')
        if id is not None:
            obj = Recipe.objects.get(id=id)
        return obj
    
    def get(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = RecipeForm(instance = obj)
            context["form"] = form
            context["object"] = obj
        return render(request, self.template_name, context)
    
    def post(self, request, id = None, *args, **kwargs):
        obj = self.get_object()
        if obj is not None:
            print("Testing")
            form = RecipeForm(request.POST,instance = obj)
            form.save()
        return redirect('main:recipe_list')

# Delete for recipe 
@login_required(login_url='/login/')
# @admin_only
def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk = pk)
    recipe.delete()
    return redirect('main:recipe_list')


# Search functionalities
def get_data_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        recipes = Recipe.objects.filter(
               Q(recipe_title__icontains = q)
            )
        for recipe in recipes:
            queryset.append(recipe)

    return list(set(queryset))


