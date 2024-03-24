from django.shortcuts import render
from django.http.response import JsonResponse
from django.http.response import HttpResponse
from rest_framework.decorators import api_view
from .serializers import *
from .models import *
from rest_framework import status
from rest_framework.response import Response
import plotly.graph_objs as go
from plotly.offline import plot
from .serializers import StudentSerializer  # Import serializer if defined
from django.shortcuts import reverse
import requests
from json import JSONDecodeError


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
        return render(request, 'home/home.html', {'api_data': student})


def student_register_display(request):
    context = {}
    return render(request, 'home/student/student_register.html', context)


def student_performance_display(request):
    context = {}
    return render(request, 'home/student/student_performance.html', context)


@api_view(['GET'])
def get_student_data(request, student_id):
    try:
        student_data = Student.objects.get(student_id=student_id)
        if not student_data:
            return Response({'message': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        if not request.accepted_renderer.format == 'application/json':
            return Response({'message': 'Unsupported content type'}, status=status.HTTP_406_NOT_ACCEPTABLE)

        if hasattr(Student, 'objects'):  # Check if serializer is defined
            serializer = StudentSerializer(student_data)
            return Response(serializer.data)
        else:
            # Return data as a dictionary if no serializer defined
            return Response({
                'total_warnings_number': student_data.total_warnings_number,
            })
    except Student.DoesNotExist:
        return Response({'message': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)


# def my_view(request):
#     context = {}  # Create a context dictionary to pass data to the template (optional)
#     return render(request, 'student.html', context)  # Render the template