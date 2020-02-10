from django.urls import path
from. import views

urlpatterns = [

     path('feedback/contact/', views.contact, name='contact'),

]
