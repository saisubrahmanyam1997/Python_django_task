from django.urls import path
from analysis import views
from .views import student_list, student_marks

urlpatterns = [
    path('student/', views.student_list, name= "student_list"),
    path('student/result/', views.student_marks, name= "student_marks")
]
