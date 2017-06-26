# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def portfolio_list(request):
	posts = Post.objects.all()
	return render(request, 'portfolio/portfolio_list.html', {'posts':posts})

def portfolio_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'portfolio/portfolio_detail.html', {'post': post})

@login_required
def portfolio_create(request):
	form = PostForm()
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('portfolio_detail', pk=post.pk)
	else:
 		form = PostForm()
    	return render(request, 'portfolio/portfolio_edit.html', {'form': form})		

@login_required
def portfolio_edit(request, pk):
	post=get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('portfolio_detail', pk=post.pk)	
	else:
		form = PostForm(instance=post)
		return render(request, 'portfolio/portfolio_edit.html', {'form':form})

def portfolio_your_content(request):
	posts = Posts.object.filter_by()

