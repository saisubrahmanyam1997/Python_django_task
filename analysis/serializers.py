from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
   class Meta:
       model = Student
       fields = ['id', 'Name', 'Roll_Number', 'Date_of_Birth']
       #fields = '__all__'

class StudentMarksSerializer(serializers.ModelSerializer):
   class Meta:
       model = Student
       
       fields = '__all__'       
