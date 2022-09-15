from django.urls import path, include
from accounts import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.RegistrationUser.as_view(), name='register'),
]
