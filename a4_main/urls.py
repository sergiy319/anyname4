from django.urls import path
from . import views

urlpatterns = [
    path('', views.first_page_character_entry),
    path('word_length', views.choice_word_length),
    path('sorting_results', views.displaying_sorting_results),
    path('meaning_words', views.explanation_meaning_words),
]
