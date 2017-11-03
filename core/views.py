from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'title': 'Django E-commerce'
    }
    return render(request, 'index.html', context)

