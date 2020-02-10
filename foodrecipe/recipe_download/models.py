from django.db import models

# Create your models here.
class Recipe_Video(models.Model):
    title = models.CharField(max_length = 50)
    name = models.CharField(max_length = 50)
    info = models.CharField(max_length = 200)
    videos = models.FileField(upload_to = "recipe_videos/", null=True, verbose_name = "")
    datetime = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name + ": " + str(self.videos)
