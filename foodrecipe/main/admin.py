from django.contrib import admin
from .models import User, Recipe, Comment, Item

admin.site.register(User)
admin.site.register(Recipe)
admin.site.register(Comment)
admin.site.register(Item)

