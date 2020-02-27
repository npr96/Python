# def word_reverser(word_to_reverse):
#     word_container = []
#     for i in word_to_reverse:
#         word_container = i.split() + word_container
#     word_container = map(str, word_container)
#     reversed_word = ''.join(word_container)
#     print(reversed_word)
# word = 'people are people, so why should it be, you and I should get along so awfully?'
# word_reverser(word)

def median_finder(list_to_find_median_of):
    indicator_even_odd = len(list_to_find_median_of) % 2
    sorted(list_to_find_median_of)
    if indicator_even_odd == 0:
        middle_index = (len(list_to_find_median_of) / 2) - 1
        middle_index_2 = (middle_index + 1)
        result_double = list_to_find_median_of[int(middle_index)] + list_to_find_median_of[int(middle_index_2)] 
        result = float(result_double) / 2
        return result
    if indicator_even_odd == 1:
        middle_index = ((len(list_to_find_median_of) / 2) + 0.5)
        return list_to_find_median_of[int(middle_index)]

print(median_finder([1,2,3,4,5,6,7,8,9]))