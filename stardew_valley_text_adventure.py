import random
import cmd
import sys
dictionary_of_places = {
    'home': '''''',
    'farm': '''''',
    'town': '''''',
    'store': '''''',
    'bar': ''''''
}
dictionary_of_familiar_places = {
    'home': 'You Return Home',
    'farm': 'You Go To Work On Your Farm',
    'town': 'You Arrive Back In Town',
    'store': 'Pierre greets you',
    'bar': 'You Arrive at the Bar'
}
dictionary_of_prices = {
    'potato seeds': 1,
}
dictionary_of_quantity = {
    'potato seeds': 15,
}
dictionary_of_grow_times = {

}
dictionary_of_events = {

}
dictionary_of_responces = {

}
dictionary_of_actions = {

}
dictionary_of_been_there = {
    'home': 0,
    'farm': 0,
    'town': 0,
    'store': 0,
    'bar': 0
}
def goto_if_declutter(arg):
    if stardew_valley.dictionary_of_been_there_local[arg] == 0:
        print(dictionary_of_places[arg])
        stardew_valley.dictionary_of_been_there_local[arg] = 1
        return
    elif stardew_valley.dictionary_of_been_there_local[arg] == 1:
        print(dictionary_of_familiar_places[arg])
        return
    else:
        stardew_valley.dictionary_of_been_there_local[arg] = 0
        print('Something went wrong, please try again')
        return
location = 'home'
town_loc = 'main'
wallet = 10


buy_error = 'You can\'t buy that here, to find out what you can buy, go to the store and type \'stock\''
class stardew_valley(cmd.Cmd):
    intro = '''
You arrive at your grandfather\'s old farm and see an old man wearing a plad beret standing in front of the door. 
The house looks small but well kept and cozy. The old man turns as you arrive and greets you with a smile and a 
handshake.
\"The name is Lewis, I am mayor around these parts.\"
\"So you are the old boys grandchild\"
\"He told me he was leaving you the place before he died, welcome to town, I hope you will like it here\"
\"Please introduce yourself to the townsfolk, they are friendly people.\"
\"If you need anything, you can probably find it at Pierre's store in town\"
\"Also, if you need anything taken to market, you can put it in that crate over there and I will take it for you\"
\"If you ever get stuck try typing help to find out what you can do.\"
After shaking your hand again Old man Lewis leaves down the road to town.

You are left standing infront of you new home (type 'goto home' to enter)
'''
    prompt = '-Stardew-'
    file = None
    dictionary_of_inventory = {
        'potato seeds': 0,
        'hops seeds': 0,
        'daisy': 0,
    }
    dictionary_of_been_there_local = dictionary_of_been_there
    purchase_indicator = ''
    location_local = location
    town_loc_local = town_loc
    wallet_local = 10
    shopping_cart = 0

    def do_goto(self, arg):
        if arg == 'farm' or arg == 'home' or arg == 'town':
            stardew_valley.location_local = arg
            stardew_valley.town_loc_local = 'main'
            goto_if_declutter(arg)
            return
        if arg == 'store' or arg == 'bar':
            if stardew_valley.location_local == 'town':
                stardew_valley.town_loc_local = arg
                goto_if_declutter(arg)
                return
            else:
                print('You need to be in town first!')
                return
        else:
            print('Stardew didn\'t understand where you wanted to go,'
                  '\nTry typeing \'goto\' followed by \'farm\', \'home\', \'town\', \'store\', or \'bar\'')

    def do_stock(self):
        print(dictionary_of_prices.keys())

    def do_buy(self, arg):
        if stardew_valley.town_loc_local != 'store':
            print('You need to be in Pierre\'s store to buy! try going to town, then store')
            return
        elif stardew_valley.town_loc_local == 'store':
            if arg in dictionary_of_prices.keys():
                stardew_valley.purchase_indicator = arg
                print(
                    'The Price of ' + str(stardew_valley.purchase_indicator) + ' is ' +
                    str(dictionary_of_prices[stardew_valley.purchase_indicator]) + ' how many would you like to buy ' +
                    'type \'amount x\''
                )
                return
            else:
                print(buy_error)
                return

    def do_amount(self, arg):
        if isinstance(int(arg), int):
            stardew_valley.shopping_cart = int(arg) * dictionary_of_prices[stardew_valley.purchase_indicator]
            if stardew_valley.wallet_local >= stardew_valley.shopping_cart:
                print('You buy ' + str(arg) + ' of ' + str(stardew_valley.purchase_indicator))
                stardew_valley.shopping_cart = int(arg) * dictionary_of_prices[stardew_valley.purchase_indicator]
                stardew_valley.wallet_local = stardew_valley.wallet_local - stardew_valley.shopping_cart
                stardew_valley.shopping_cart = 0
                stardew_valley.dictionary_of_inventory[stardew_valley.purchase_indicator] = (
                        dictionary_of_quantity[stardew_valley.purchase_indicator] * int(arg)
                )
                stardew_valley.purchase_indicator = ''
                return
            else:
                print('You don\'t have enough money!')
                return
        else:
            print('The amount you buy needs to be a number!')
            return

    def do_inventory(self, arg):
        for key in stardew_valley.dictionary_of_inventory:
            if stardew_valley.dictionary_of_inventory[key] > 0:
                print(str(key) + ': ' + str(stardew_valley.dictionary_of_inventory[key]))
                break
            else:
                pass


if __name__ == "__main__":
    stardew_valley().cmdloop()
