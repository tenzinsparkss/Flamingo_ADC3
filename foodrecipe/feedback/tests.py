from django.test import TestCase
from .models import Feedback

# Create your tests here.
class FeedbackTest(TestCase):
    def setUp(self):
        Feedback.objects.create(feedback_email = "karma@gmail.com", subject = "food")
        Feedback.objects.create(feedback_email = "yangji@gmail.com", subject="meat")

    def test_recipe(self):
        k = Feedback.objects.get(feedback_email = "karma@gmail.com")
        y = Feedback.objects.get(feedback_email = "yangji@gmail.com")
        self.assertEqual(k.food(), 'This user has given feedback about "food"')
        self.assertEqual(y.food(), 'This user has given feedback about "meat"')


