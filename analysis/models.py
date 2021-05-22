from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.BigAutoField(primary_key= True)
    Name = models.CharField(max_length= 32,null= False)
    Roll_Number = models.IntegerField(null= False, unique= True)
    Date_of_Birth = models.DateField(null= False)
    marks = models.PositiveIntegerField(null=True)

    
    
    
    
#Name
#Roll Number (Unique)
#Date of Birth
