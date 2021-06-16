from itertools import permutations


# users_input = 'aasdfg'
# for i in list(map("".join, permutations(users_input, 3))):
#     print(i)

# for item in permutations('aasdfg', 3):
#     print(''.join(item))

# def names_combinations(users_input, words_amount):
#     if words_amount <= len(users_input):
#         for name in list(map("".join, permutations(users_input, words_amount))):
#             print(name.capitalize())
#     else:
#         print(f'The number of letters should be no more than {len(users_input)}')
#
#
# names_combinations('Alexander', 5)

# Create a function to sort a word with one given length.
def letters_permutation(users_input, words_amount):
    names_variants = sorted(list(set([''.join(name_variant).capitalize()
                                      for name_variant
                                      in permutations(users_input, words_amount)])))
    return names_variants


# Create a function to sort words with a range of preset lengths.
def letters_permutation_range(users_input, min_amount, max_amount):
    names_variants = [letters_permutation(users_input, words_amount)
                      for words_amount in range(min_amount, max_amount + 1)]
    return names_variants


print(letters_permutation('bfFf', 4))
print(letters_permutation_range('axXx', 3, 4))
