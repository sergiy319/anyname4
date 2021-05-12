from django.shortcuts import render
from django.http import HttpResponse


# Create a method to enter a string of values.
def first_page_character_entry(request):
    return render(request, 'a4_main/first_page_character_entry_template.html')


# Create a method to determine the length of a word.
def choice_word_length(request):
    return HttpResponse("<h4>There will be a choice of word length</h4>")


# Create a method to displaying sorting results.
def displaying_sorting_results(request):
    return HttpResponse("<h4>There will be a displaying sorting results</h4>")


# Create a method to explanation of the meaning of words.
def explanation_meaning_words(request):
    return HttpResponse("<h4>There will be a explanation of the meaning of words</h4>")
