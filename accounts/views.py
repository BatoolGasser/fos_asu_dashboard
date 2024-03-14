from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.

def home(request):
    return render(request=request, template_name='index.html', context={'name':'batool', 'age':"32", 'year':''})

