from django.db import models


# Create a class to handle user string.
class User_String_Handling(models.Model):
    user_letters_set = models.CharField('letters', max_length=50)
    min_number_letters_in_word = models.IntegerField('minimum')
    max_number_letters_in_word = models.IntegerField('maximum')
    word_variants = models.TextField('variants')

    def __str__(self):
        return self.word_variants
