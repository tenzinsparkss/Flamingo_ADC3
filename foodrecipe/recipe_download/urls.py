from django.urls import path
from . import views

app_name= 'recipe_download'
urlpatterns = [

    path('browse/', views.browse, name="browse"),
    path('upload_video/', views.upload_video, name ="upload_video"),

]