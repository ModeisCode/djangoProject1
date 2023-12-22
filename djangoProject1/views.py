from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title': 'Django Homepage',
        'content': 'This is the homepage of my Django project.',
    }
    return render(request, 'index.html', context)

