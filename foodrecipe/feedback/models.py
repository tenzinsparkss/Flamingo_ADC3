from django.db import models


# Create your models here.
class Feedback(models.Model):
    full_name = models.TextField()
    feedback_email = models.EmailField()
    subject = models.CharField(max_length= 200)
    comment = models.TextField()

    def __str__(self):
        return self.full_name

