from django.shortcuts import render
from .models import Post

# Use SQL lite for developement and postgres for production

def home (request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'renoreddit/home.html', context)

def about (request):
    return render(request, 'renoreddit/about.html', {'title': 'About'})