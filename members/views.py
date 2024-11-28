from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    x={'name':'Rama'}
    return render(request,'pages/index.html', x)
def about (request):
    return render(request, 'pages/about.html' )
