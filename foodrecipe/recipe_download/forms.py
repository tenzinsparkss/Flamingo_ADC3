from django import forms
from .models import Recipe_Video

class DownloadForm(forms.ModelForm):
    class Meta:
        model = Recipe_Video
        fields = ('title', 'name', 'info', 'videos')
