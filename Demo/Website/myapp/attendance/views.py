from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def showAttendance(request):
    userId = request['data']

    return Response("")