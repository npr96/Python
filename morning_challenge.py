# def word_reverser(word_to_reverse):
#     word_container = []
#     for i in word_to_reverse:
#         word_container = i.split() + word_container
#     word_container = map(str, word_container)
#     reversed_word = ''.join(word_container)
#     print(reversed_word)
# word = 'people are people, so why should it be, you and I should get along so awfully?'
# word_reverser(word)

# def median_finder(list_to_find_median_of):
#     indicator_even_odd = len(list_to_find_median_of) % 2
#     sorted(list_to_find_median_of)
#     if indicator_even_odd == 0:
#         middle_index = (len(list_to_find_median_of) / 2) - 1
#         middle_index_2 = (middle_index + 1)
#         result_double = list_to_find_median_of[int(middle_index)] + list_to_find_median_of[int(middle_index_2)] 
#         result = float(result_double) / 2
#         return result
#     if indicator_even_odd == 1:
#         middle_index = ((len(list_to_find_median_of) / 2) + 0.5)
#         return list_to_find_median_of[int(middle_index)]

# print(median_finder([1,2,3,4,5,6,7,8,9]))

#was challenged to make it so that we can pass in any dictionary

import cmd, sys
itterator = 72
dictionary_of_odds = {
    'Winning' : 1,
    'Break Even' : 2,
    'Loss' : 3
}
dictionary_of_interpritation = {
    '1' : 'Congradulations, You Won!',
    '2' : 'You Broke Even!',
    '3' : 'Sorry, You Lost!'
}

class lottery(cmd.Cmd):
    intro = '\nWelcome to the lottery\n'
    prompt = '(lottery)'
    def do_pull(self, arg):
        winning_list = [dictionary_of_odds['Winning']] * dictionary_of_odds['Winning'] 
        break_even_list = [dictionary_of_odds['Break Even']] * dictionary_of_odds['Break Even']
        loss_list = [dictionary_of_odds['Loss']] * dictionary_of_odds['Loss']
        final_list = winning_list + break_even_list + loss_list
        global itterator
        divider = len(final_list)
        current_index = itterator % divider
        index_picker = current_index - 1
        result = final_list[index_picker]
        print(dictionary_of_interpritation[str(result)])
        itterator = itterator + len(final_list) + 7

if __name__ == '__main__':
    lottery().cmdloop()