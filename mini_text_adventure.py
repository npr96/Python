def hello():
    print('howdy')
    return

def shadow():
    power_switch = 1
    while power_switch == 1:
        player_input = input()
        if player_input == 'hello':
            hello()
        else:
            pass

shadow()

