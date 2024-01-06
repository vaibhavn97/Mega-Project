from django.urls import path
from .views import showAttendance


urlpatterns = [
    path('show', showAttendance)
]