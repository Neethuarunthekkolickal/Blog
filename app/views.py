from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from . models import Post
from . forms import MakePost


def index(request):
    post = Post.objects.all()
    contex = {
        'post':post
    }
    return render(request,"index.html",contex)
@login_required
def post(request):
    form=MakePost()
    if request.method == 'POST':
        form = MakePost(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form=MakePost()
            return render(request,"post.html",{"form":form})
    return render(request,"post.html",{"form":form})
def singup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("singup")
    return render(request,"singup.html",{"form":form})
