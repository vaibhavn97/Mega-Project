from django.db import models
from subjectsapp.models import Course

# Create your models here.
class ClassRoom(models.Model):
    no = models.IntegerField()
    inUse = models.BooleanField(default=False)
    course = models.ForeignKey(to=Course, on_delete=models.DO_NOTHING, default=models.NOT_PROVIDED)

    def __str__(self) -> str:
        return f"ClassRoom {self.no}   -- {self.inUse} -- {self.course}"