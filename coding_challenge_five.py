# def string_of_ommission():
#     ommit_these = [1, 2, 3]
#     itterator_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,16,17,18,19,20]
#     result = []
#     for i in itterator_list:
#         if i in ommit_these:
#             x = 1
#         else:
#             result = result + [i]
#     print(result)
#
#
#
# string_of_ommission()

# header_constraint = [1, 2, 3, 4, 5, 6]


# def heading_generator(text, h_type):
#     return f'<h{my_type}>{my_text}</h{my_type}>'
#
#
# print(heading_generator("greeting", 2))

def fizz_buzz(max_number):
    pre_change_list = list(range(1, max_number + 1))
    result_list = []
    for i in pre_change_list:
        if int(i) % 3 == 0 and int(i) % 5 == 0:
            result_list = result_list + ['fizzbuzz\n']
        elif int(i) % 3 == 0:
            result_list = result_list + ['fizz\n']
        elif int(i) % 5 == 0:
            result_list = result_list + ['buzz\n']
        else:
            result_list = result_list + [str(i) + '\n']
    result_list = ' '.join(result_list)
    return result_list

print(fizz_buzz(100))