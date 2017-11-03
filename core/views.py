from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    texts = ['lorem ipsum', 'Lorem Ipsum é simplesmente uma simulação de texto da indústria tipográfica e de impressos, e vem sendo utilizado desde o século XV']
    context = {
        'title': 'Django E-commerce',
        'texts': texts
    }
    return render(request, 'index.html', context)
