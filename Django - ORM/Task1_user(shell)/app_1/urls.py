from django.urls import path
from . import models

urlpatterns = [
    path('',models.Users),  
]
