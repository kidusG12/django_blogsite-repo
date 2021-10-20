from django.db import models
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,DetailView

# Create your views here.
# def home(request):
#     context = {
#         'posts': Post.objects.all(),
#         'title':'Home',
#         }
#     return render(request, "blog/home.html", context)


class PostListView(ListView):
    model = Post
    template_name = "blog/home.html" 
    context_object_name = 'posts'
    ordering = ['-posted_date']


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'


def about(request):
    context = {
        'title':'Home',
        }
    return render(request, "blog/about.html", context)