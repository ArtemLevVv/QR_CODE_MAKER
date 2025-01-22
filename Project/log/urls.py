from .views import *
from django.urls import path

urlpatterns = [
    path('', render_log, name='log'),
    # path('/reg', render_reg, name='reg'),
]
