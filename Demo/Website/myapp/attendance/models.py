from django.db import models
import datetime 
from subjectsapp.models import Course
from django.contrib.auth.models import User

# Create your models here.
class Attendance(models.Model):
    year = models.IntegerField(default=datetime.datetime.now().year)
    lecture_no = models.CharField()
    course = models.ForeignKey(to=Course, on_delete=models.DO_NOTHING)
    teacher = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)