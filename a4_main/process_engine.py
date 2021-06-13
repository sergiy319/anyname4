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


def names_combinations(users_input, words_amount):
    names_variants = sorted(list(set([''.join(name_variant).capitalize()
                                      for name_variant in permutations(users_input, words_amount)])))
    return names_variants


def names_range_number_letters(users_input, minimum_letters, maximum_letters):
    any_names_variants = [names_combinations(users_input, words_amount)
                          for words_amount in range(minimum_letters, maximum_letters + 1)]
    return any_names_variants
