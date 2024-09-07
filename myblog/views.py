from django.shortcuts import render,get_object_or_404,redirect
from . import models

from . import forms
from django.contrib.auth import login,logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
def homepage(request):
    bloglar = models.movies.objects.all()
    return render(request,'home.html',{'postlar':bloglar})


def registration(request):
    if request.method =='POST':
        form  = forms.RegForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
    else:
        form  = forms.RegForm()
    return render(request,'reg.html',{'form':form})



def sign_in(request):
    if request.method =='POST':
        form  = forms.LoginForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('home')
    else:
        form  = forms.LoginForm()
    return render(request,'login.html',{'form':form})

def log_out(request):
    logout(request)
    return redirect('home')

def detail(request,id):
    post = get_object_or_404(models.movies,id=id)
    comments = models.Comments.objects.filter(movie=post)
    if request.method=='POST':
        comment_form = forms.commentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.movie = post
            new_comment.username = request.user
            new_comment.save()
            return redirect('detail',id=post.id)
    else :
            comment_form = forms.commentForm()
    return render(request,'detail.html',{'post':post,'comments':comments,'comment_form':comment_form})



@login_required

def update_post(request,id):
    blog_post=get_object_or_404(models.movies,id=id)
    if blog_post.author!=request.user:
        return redirect('home')
    model = models.movies.objects.get(id=id)
    form = forms.BlogForm(request.POST or None,request.FILES,instance=model)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request,'update_post.html',{'form':form , 'model':model})

@login_required
def delete_post(request,id):
    blog_post = get_object_or_404(models.movies,id=id)
    if blog_post.author!=request.user:
        return redirect('home')
    model = models.movies.objects.get(id=id)
    form = forms.BlogForm(request.POST or None,request.FILES,instance=model)
    if request.method=='POST':
        model.delete()
        return redirect('home')
    return render(request,'delete.html',{'form':form})

