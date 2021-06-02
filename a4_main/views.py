from django.shortcuts import render


# Create a method to enter a string of values.
def input_param(request):
    return render(request, 'a4_main/input_param.html')


# Create a method to explanation of the meaning of words.
def output_result(request):
    return render(request, 'a4_main/output_result.html')
