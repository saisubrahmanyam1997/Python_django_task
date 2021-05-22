from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Student
from .serializers import StudentMarksSerializer, StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status
from django.db.utils import OperationalError

# Create your views here.

@api_view(['GET', 'POST'])
def student_list(request):
    if request.method == 'GET':
        student = Student.objects.all()
        serializer = StudentSerializer(student, many =True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)         
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)   
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def student_marks(request):
    if request.method == 'GET':
        student = Student.objects.all()
        serializer = StudentMarksSerializer(student, many =True)
        return Response(serializer.data)
    elif request.method == 'POST':
        rollnum = request.POST.get('rollnum')
        marks = request.POST.get('marks')

        try:
            Student.objects.filter(Roll_Number=rollnum).update(marks = marks)
        except OperationalError as oe:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(status=status.HTTP_200_OK)   


