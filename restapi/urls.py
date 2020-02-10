from django.urls import path
from . import views

app_name= 'restapi'

urlpatterns = [
    path('api/', views.api_data, name="api_data"),
    path('change/<int:pk>/', views.update_api_data, name=" update_api_data"),
    path('api_recipe/<int:PAGENO>/<int:SIZE>', views.api_recipe, name="api_recipe"),
    path('new/', views.api_add_recipe, name = "api_add_recipe"),

]