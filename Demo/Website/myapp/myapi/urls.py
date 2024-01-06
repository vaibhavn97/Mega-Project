from django.urls import path
from .views import recognizeFace, isStudent, verifyToken, MyObtainTokenPairView, getPrnCode
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('recognizeface', recognizeFace),
    path('isstudent/', isStudent),
    path('create', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('getprncode', getPrnCode),
    path('verify', verifyToken, name='token_verify'),

]