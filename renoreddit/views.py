from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author': 'Misko',
        'title': 'Subway tile install',
        'content': 'Installing subway tile is annoying. Pick a large tile!',
        'date': 'January 19, 2024'
    },
        {
        'author': 'Lia-Marie',
        'title': 'Shiplap: Still in Style',
        'content': 'Going for a farmhouse look? Give it a try!',
        'date': 'January 15, 2024'
    }
]

def home (request):
    context = {
        'posts': posts
    }
    return render(request, 'renoreddit/home.html', context)

def about (request):
    return render(request, 'renoreddit/about.html', {'title': 'About'})