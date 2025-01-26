from .views import *
from django.urls import path

urlpatterns = [
    path('qr_code_generation/', render_ger, name='ger'),
    path('my_qr_code/', render_my_qr, name='my_qr'),
]