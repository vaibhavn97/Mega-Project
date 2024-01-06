from django.urls import path
from .views import getAvail, setAvail, clearAvail, checkAvail

urlpatterns = [
    path('getAvail', getAvail),
    path('setAvail', setAvail),
    path('clearAvail', clearAvail),
    path('checkAvail', checkAvail),

]