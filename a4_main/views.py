from django.shortcuts import render
from .models import User_String_Handling


# Create a method to enter a string of values.
def input_param(request):
    return render(request, 'a4_main/input_param.html')


# We create a method for showing variants and meanings of words.
def output_result(request):
    return render(request, 'a4_main/output_result.html')
