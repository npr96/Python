#division functionality broken fix at home
opperator_modifier = None
dynamic_reducer_list = [1,2,3]
iterated_value = 0 
division_helper_variabl = 1
printed_division = 0
def dynamic_reducer(dynamic_reducer_list, opperator_modifier):
    global printed_division
    global iterated_value
    if opperator_modifier == '+':
        for i in dynamic_reducer_list:
            iterated_value = iterated_value + i
        print(iterated_value)
    elif opperator_modifier == '-':
        for i in dynamic_reducer_list:
            iterated_value = iterated_value - i
        print(iterated_value)
    elif opperator_modifier == '*':
        iterated_value = 1
        for i in dynamic_reducer_list:
            iterated_value = iterated_value * i
        print(iterated_value)
    elif opperator_modifier == '/':
        for i in dynamic_reducer_list:
            division_helper_variabl = i
            division_result = iterated_value // division_helper_variabl
            iterated_value = i
            printed_division = printed_division + division_result
        print(printed_division)
    else:
        return "something went wrong" 
dynamic_reducer([1,2,3],'/')     
    

    