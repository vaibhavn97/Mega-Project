from django.urls import path
from .views import getStudent, getStaff, getData

urlpatterns = [
    path('student', getStudent),
    path('staff', getStaff),
    path('userdata', getData)
]