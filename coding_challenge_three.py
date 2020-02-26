def manual_exponent_function(base, power):
    iterator = 1
    product_container = 1
    while iterator <= power:
        product_container = base * product_container
        iterator = iterator + 1
    print(product_container)

manual_exponent_function(3,3)

def manual_exponent_function_two(base,power):
    base_string = [base] * power
    product_container = 1
    for i in base_string:
        product_container = product_container * i
    print(product_container)

manual_exponent_function_two(3,3)

from functools import reduce

def manual_exponent_function_three(base,power):
    iterator = [base] * power
    result = reduce(lambda x, y : x * y, iterator)
    print(result)

manual_exponent_function_three(3,3)
