#division functionality does not float fix at home
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
        iterated_value = dynamic_reducer_list[0]
        for index, i in enumerate(dynamic_reducer_list):
            if index < 1:
                iterated_value = i
            if index >= 1:
                iterated_value = iterated_value / i
        print(iterated_value)
    else:
        return "something went wrong" 
dynamic_reducer([12,2,3],'/')     
    

    