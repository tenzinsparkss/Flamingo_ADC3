from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import DownloadForm
from . models import Recipe_Video


# Create your views here.
@login_required(login_url='/login/')
def browse(request):
    recipe_video = Recipe_Video.objects.all()
    return render(request, 'recipe_download/browse.html',{'recipe_videos': recipe_video})

@login_required(login_url='/login/')
def upload_video(request):
    form = DownloadForm()
    if request.method == "POST":
        form = DownloadForm(request.POST, request.FILES)
        if form.is_valid():
            if request.user:
                form.save()
            else:
                messages.success(request, f'Please enter a correct email and password.')
                return render(request, "main/login.html")
            return redirect('recipe_download:browse')
    return render(request, "recipe_download/upload_video.html", {"form" : form})
