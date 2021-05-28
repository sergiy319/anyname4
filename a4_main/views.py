from django.shortcuts import render


# Create a method to enter a string of values.
def first_page_character_entry(request):
    return render(request, 'a4_main/entry.html')


# Create a method to determine the length of a word.
def choice_word_length(request):
    return render(request, 'a4_main/choice.html')


# Create a method to displaying sorting results.
def displaying_sorting_results(request):
    return render(request, 'a4_main/sorting.html')


# Create a method to explanation of the meaning of words.
def explanation_meaning_words(request):
    return render(request, 'a4_main/explanation.html')
