from django.urls import path
from api.views import *

urlpatterns = [
    path('analisador', analisys, name='process-input'),
    path('parser', parser, name='process-parser'),
]