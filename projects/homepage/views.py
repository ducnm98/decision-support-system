from django.shortcuts import render, HttpResponse, loader
from datetime import datetime

def index(request):
    context = {
        'today': datetime.now()
    }
    return render(request, 'homepage/index.html', context)