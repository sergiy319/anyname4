from django.urls import path
from . import views

urlpatterns = [
    path('', views.first_page_character_entry),
    path('choice', views.choice_word_length),
    path('sorting', views.displaying_sorting_results),
    path('explanation', views.explanation_meaning_words),
]
