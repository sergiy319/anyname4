from .models import User_String_Handling
from django.forms import ModelForm, TextInput


class User_String_Handling_Form(ModelForm):
    class Meta:
        model = User_String_Handling
        fields = [
            'user_letters_set',
            'min_number_letters_in_word',
            'max_number_letters_in_word',
        ]
        widgets = {
            'user_letters_set': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a set of letters or a word:'
            }),
            'min_number_letters_in_word': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the minimum number of letters in the word:'
            }),
            'max_number_letters_in_word': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the maximum number of letters in the word:'
            }),
        }
