from django.shortcuts import render
from django.http.response import JsonResponse
from django.http.response import HttpResponse
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
import requests
from json import JSONDecodeError

from .models import *


# Create your views here.

# This is A Test
def home(request):
    return HttpResponse("Helloooo From Users")


# api to get the data in the django views
@api_view(['GET', 'PUT', 'DELETE'])
def FBV_pk(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # GET
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)


@api_view(['GET'])
def get_data_pk(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # GET
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return render(request, 'home.html', {'api_data': student})
