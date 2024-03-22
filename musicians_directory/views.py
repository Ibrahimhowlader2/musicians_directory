from django.views import View
from django.shortcuts import render
from album.models import Album
from django.views.generic import ListView

class homeView(ListView):
    template_name="home.html"
    model=Album
    context_object_name='data'
    

