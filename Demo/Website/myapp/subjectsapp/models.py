from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)


    def __str__(self) -> str:
        return f"{self.name} -- {self.code} -- {self.teacher}"



class Enrolled(models.Model):
    student = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)
    course = models.ForeignKey(to=Course, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f"{self.student} enrolled for {self.course}"