from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .models import Enrolled, Course

# Create your views here.
@api_view(['GET', "POST"])
def getStudent(request):
    usr = User.objects.get(id = request.data['userId'])
    enIt = Enrolled.objects.filter(student=usr)
    lis = []
    for item in enIt:
        name = item.course.name
        code = item.course.code
        lis.append(f"{name} -- {code}")
    print(lis)
    return Response({
        "data": lis
    })

@api_view(['GET', "POST"])
def getStaff(request):
    usr = User.objects.get(id = request.data['userId'])
    enIt = Course.objects.filter(teacher=usr)
    lis = []
    for item in enIt:
        name = item.name
        code = item.code
        lis.append(f"{name} -- {code}")
    print(lis)
    return Response({
        "data": lis
    })

@api_view(['GET', "POST"])
def getData(request):
    usr = User.objects.get(id = request.data['userId'])
    return Response({
        "first_name" : usr.first_name,
        "last_name" : usr.last_name,
        "email" : usr.email
    })
