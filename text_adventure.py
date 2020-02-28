import cmd, sys
room_number = 1
dark_indicator = 'light'
dictionary_of_inspection = {
    '1bed' : '''the mattress is dingy and in bad repare, you can see the springs in several places, \n
the bed is obviously stained with puke and urine, although it looks like someone \n
has gone through some effort to clean it.''',
    '1door' : 'A wooden door with a brass doorknob, you can see light seeping in under the door',
    '1table' : 'A small bedside table with two drawers, and a leaf on top, the drawers are empty',
    '1leaf' : 'A small oak leaf with a dark green color, you notice the veins are quite dark.',
    '2table' : 'The table is about 3ft in diameter, has three legs, and is wobbly',
    '2cup' : 'The cup is plastic and empty',
    '2plate' : 'The plate is clean, but it\'s edges are chipped.',
    '2painting' : '''The paiting is well made, in contrast with the bare wall it hangs on, the snake \n
is coiled arround a person\'s arm which is visible in the frame from the arm up. The hand\n
is holding an appple. ''',

}
dictionary_of_rooms = {
    "1" : '''You awake in a small dark room, a dim pre-dawn or twilight light filteres through a \n
shuttered window, you are lying on a bare bed that smells strongly of vomit, you notice a\n
door to your right''',
    "2" : '''The room is about ten-feet-square with a single dim and flickering bulb hanging from the ceiling\n
underneath the bulb is a rickety table with a plate, cup, and spoon on top. There is also a\n
Cassio watch on the table, the floor is carpeted but threadbare, and there is a painting \n
of a snake on the wall''',
}
dictionary_of_interaction = {
    "1door" : 'The door swings open easily and you enter the room on the other side\n',
    '2bulb' : 'Ouch! the bulb is hot! You unscrew it anyway, and the lights go out.',
}

        
class TextAdventure(cmd.Cmd):
    intro = '''\nWelcome to TextAdventure!   Type ? or help for a list of commands. \n
    \n
You awake in a small dark room. a dim pre-dawn or twilight light filteres through a \n
shuttered window, you are lying on a bare bed that smells strongly of vomit, you notice a\n
door to your right and a table to your left. \n'''
    prompt = '(text)'
    file = None
    room_number = 1
    def do_inspect(self, arg):
        print(dictionary_of_inspection[modify_input(arg)])
    def do_interact(self, arg):
        if arg == 'door':
            print(dictionary_of_interaction[modify_input(arg)])
            global room_number
            room_number = room_number + 1
            print(dictionary_of_rooms[str(room_number)])
        elif arg == bulb:
            if dark_indicator == 'light':
                global dark_indicator
                dark_indicator = 'dark'
            else:
                global dark_indicator
                dark_indicator == 'light'
            print(dictionary_of_interaction[modify_input(arg)])
        elif dark_indicator == dark:
            print('You cannot see what you are doing')
        else:
            print(dictionary_of_interaction[modify_input(arg)])
    def do_back(self):
        print('You return to the previous room')
        global room_number
        room_number = room_number - 1


def modify_input(arg):
    return str(str(room_number) + str(arg))

if __name__ == '__main__':
    TextAdventure().cmdloop()