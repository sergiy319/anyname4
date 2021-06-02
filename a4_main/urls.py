from django.urls import path
from . import views

urlpatterns = [
    path('', views.input_param, name='input'),
    path('output', views.output_result, name='output'),
]
