from django.http import HttpResponse
from django.shortcuts import render
import json

def user_profiles(request):
    # Görünümün iş mantığını buraya ekleyin.
    context = {}
    return render(request, 'profiles.html', context)