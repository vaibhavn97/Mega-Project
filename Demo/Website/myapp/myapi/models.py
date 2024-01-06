from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='profile')
    rfid_code = models.CharField(max_length = 20, default="")
    
    def __str__(self) -> str:
        return f'{self.user}'