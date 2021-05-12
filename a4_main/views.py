from django.shortcuts import render


# Create a method to enter a string of values.
def first_page_character_entry(request):
    return render(request, 'a4_main/first_page_character_entry_template.html')


# Create a method to determine the length of a word.
def choice_word_length(request):
    return render(request, 'a4_main/choice_word_length_template.html')


# Create a method to displaying sorting results.
def displaying_sorting_results(request):
    return render(request, 'a4_main/displaying_sorting_results_template.html')


# Create a method to explanation of the meaning of words.
def explanation_meaning_words(request):
    return render(request, 'a4_main/explanation_meaning_words_template.html')
