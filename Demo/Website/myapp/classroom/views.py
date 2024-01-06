from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ClassRoom
from subjectsapp.views import Course
from django.http import HttpResponse

# Create your views here.
@api_view(['GET', 'POST'])
def getAvail(request):
    # classroomNumber = int(request.data['classroomNumber'])
    # # classroomNumber = 13
    # print(f"Code is {classroomNumber}")
    data = ClassRoom.objects.filter()
    lis = ["0"]
    for item in data:
        lis.append(f"{item.no}")

        
    return Response({
        "data" : lis
    })

    
@api_view(['GET', 'POST'])
def setAvail(request):
    classroomNumber = int(request.data['classroomNumber'])
    courseCode  = request.data['courseCode'].split(' -- ')[1]
    # print(classroomNumber, courseCode)
    courseName = Course.objects.get(code = courseCode)
    classRoomObject = ClassRoom.objects.get(no=classroomNumber)
    print(classRoomObject)
    classRoomObject.inUse = True
    classRoomObject.course = courseName
    classRoomObject.save()
    return HttpResponse("OK")

@api_view(['GET', 'POST'])
def clearAvail(request):
    classroomNumber = int(request.data['classroomNumber'])
    courseCode  = request.data['courseCode'].split(' -- ')[1]
    # print(classroomNumber, courseCode)
    courseName = Course.objects.get(code = courseCode)
    classRoomObject = ClassRoom.objects.get(no=classroomNumber)
    print(classRoomObject)
    classRoomObject.inUse = False
    classRoomObject.course = courseName
    classRoomObject.save()
    return HttpResponse("OK")



@api_view(['GET', 'POST'])
def checkAvail(request):
    classroomNumber = int(request.data['classroomNumber'])
    classRoomObject = ClassRoom.objects.get(no=classroomNumber)
    if classRoomObject.inUse:
        return HttpResponse("OK")
    
    return HttpResponse("NO_OK")
    
    