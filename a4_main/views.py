from django.shortcuts import render, redirect
from .forms import User_String_Handling_Form


# Create a method to enter a string of values.
def input_param(request):
    error = ''
    if request.method == 'POST':
        form = User_String_Handling_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('output')
        else:
            error = 'The form was not correct'

    form = User_String_Handling_Form()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'a4_main/input_param.html', context)


# We create a method for showing variants and meanings of words.
def output_result(request):
    return render(request, 'a4_main/output_result.html')
