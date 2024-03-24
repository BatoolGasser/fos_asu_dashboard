from django.shortcuts import render
from django.http.response import HttpResponse
from accounts.login import UserLoginForm


def home(request):
    return render(request=request, template_name='accounts/index.html', context={'name':'batool', 'age':"32", 'year':''})


def user_login(request):
    return render(request=request, template_name='accounts/user_login.html', context={'myform': UserLoginForm})


