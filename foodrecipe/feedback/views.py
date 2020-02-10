from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404

from main.admin import User
from .models import Feedback



# Create your views here.
def home(request):
    return render(request,"main/index.html")

def contact(request):

    if request.method =="POST":
        full_name=request.POST['full_name']
        feedback_email  =request.POST['feedback_email']
        subject  =request.POST['subject']
        comment =request.POST['comment']
        feedback=Feedback(full_name=full_name,feedback_email=feedback_email,subject=subject,comment=comment)
        feedback.save()
    else:
        pass
    return render(request, 'feedback/contact.html')
# def contact(request):    
#     comments = Feedback.objects.all()
#     print(comments)
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.save()

#             print(comments)

#         return redirect('main:home')

    
#     form = ContactForm()
#     return render(request, 'feedback/contact.html', {'form':form})