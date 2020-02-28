import cmd, sys
dictionary_of_places = {

}
dictionary_of_familiar_places = {

}
dictionary_of_prices = {

}
dictionary_of_grow_times = {

}
dictionary_of_events = {

}
dictionary_of_responces = {

}
dictionary_of_actions = {

}
class Stardew_Valley(cmd.Cmd):
    intro = '''
You arrive at your grandfather\'s old farm and see an old man wearing a plad beret standing in front of the door. The house looks
small but well kept and cozy. The old man turns as you arrive and greets you with a smile and a handshake.
\"The name is Lewis, I am mayor around these parts.\"
\"So you are the old boys grandchild\"
\"He told me he was leaving you the place before he died, welcome to town, I hope you will like it here\"
\"Please introduce yourself to the townsfolk, they are friendly people.\"
\"If you need anything, you can probably find it at Pierre's store in town\"
\"Also, if you need anything taken to market, you can put it in that crate over there and I will take it for you\"
\"If you ever get stuck try typing help to find out what you can do.\"
After shaking your hand again Old man Lewis leaves down the road to town.
'''
    prompt =  '-Stardew-'
    file = None

if "__name__" == "__main__":
    Stardew_Valley.cmdloop()
