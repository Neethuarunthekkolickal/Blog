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
def singup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("singup")
    return render(request,"singup.html",{"form":form})
def show(request,id):
    post = Post.objects.get(id=id)
    return render(request,"show.html",{"post":post})
@login_required
def delete(request,id):
    post=Post.objects.get(id=id)
    if request.method=="POST":
        post.delete()
        return redirect("index")
@login_required    
def edit(request,id):
    post=Post.objects.get(id=id)
    form=MakePost(instance=post)
    if request.method=="POST":
        form=MakePost(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return redirect("index")
    return render(request,"edit.html",{"form":form})
   
    
