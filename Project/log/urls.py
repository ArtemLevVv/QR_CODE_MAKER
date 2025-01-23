from .views import *
from django.urls import path

urlpatterns = [
    path('login/', render_log, name='login'),
    path('register/', render_reg, name='register'),
]
