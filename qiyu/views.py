from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    if request.method == 'GET':
        return HttpResponse('this is index page')