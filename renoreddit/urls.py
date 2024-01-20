from django.urls import path
from . import views

# Similar to creating routes in node, the program will search the urls.py file in the main file reddit_clone

urlpatterns = [
    path('', views.home, name='renoreddit-home'),
    path('about/', views.about, name='renoreddit-about'),
]
