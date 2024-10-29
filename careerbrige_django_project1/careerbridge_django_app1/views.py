from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.
#def home(request):
    #return HTTPResponse("welcome to Django Training At CareerBridge....")


def index (request):
    our_dict={'insert_CarrerBridge':"Carrer Bridge Django Training Coming from views.py file of Django App..."}
    return render(request,'careerbridge_django_app1/index.html',context=our_dict)


def student_table(request):
    students = Student.objects.all()
    return render(request, 'careerbridge_django_app1/student_table.html',{'students':students})


