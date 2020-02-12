from django.test import TestCase
from . models import Recipe_Video


# Create your tests here.
class DownloadTest(TestCase):
    def setUp(self):
        Recipe_Video.objects.create(title="spaghetti", name = "pasta")
        Recipe_Video.objects.create(title="chicken sizzler", name = "sizzler")

    def download_test(self):
        spaghetti = Recipe_Video.objects.get(title="spaghetti")
        chicken = Recipe_Video.objects.get(title="chicken sizzler")
        self.assertEqual(spaghetti.food(), 'spaghetti made of "spaghetti"')
        self.assertEqual(chicken.food(), 'chicken sizzler made of "sizzler"')
