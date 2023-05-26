from django.urls import path
from api.views import *

urlpatterns = [
    path('', analisys, name='process-input'),
]