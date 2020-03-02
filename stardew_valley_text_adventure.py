import cmd
import random
dictionary_of_places = {
    'home': '''''',
    'farm': '''''',
    'town': '''''',
    'store': '''''',
    'bar': '''''',
    'lake': ''''''
}
dictionary_of_familiar_places = {
    'home': 'You Return Home',
    'farm': 'You Go To Work On Your Farm',
    'town': 'You Arrive Back In Town',
    'store': 'Pierre greets you',
    'bar': 'You Arrive at the Bar',
    'lake': 'You Arrive at the Lake',
}
dictionary_of_prices = {
    'potato seeds': 2,
}
dictionary_of_quantity = {
    'potato seeds': 15,
}
dictionary_of_seed_conversion = {
    'potato seeds': 'potatoes'
}
dictionary_of_grow_times = {
    'potatoes' : 3
}
dictionary_of_clock = {
    1: '6:00',
    2: '7:00',
    3: '8:00',
    4: '9:00',
    5: '10:00',
    6: '11:00',
    7: '12:00',
    8: '13:00',
    9: '14:00',
    10: '15:00',
    11: '16:00',
    12: '17:00',
    13: '18:00',
    14: '19:00',
    15: '20:00',
    16: '21:00'
}
dictionary_of_events = {

}
dictionary_of_responces = {

}
dictionary_of_actions = {

}
dictionary_of_beauty = {
    0: 'You see a small ripple on the lake as a fish catches a bug',
    1: 'You notice two squirrels mating',
    2: 'You smell marrigolds on the wind',
    3: 'The wind blows gently through the trees'
}
dictionary_of_been_there = {
    'home': 0,
    'farm': 0,
    'town': 0,
    'store': 0,
    'bar': 0,
    'lake': 0
}
dictionary_of_sell_prices = {
    'potato seeds': 1
}
tuple_of_fishing = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                  29, 30, 31, 32, 33, 60, 90, 100)
dictionary_of_fishing = {
    'bass': 2,
    'rainbow_trout': 8,
    'trout': 20,
    'garbage': 100
}

player_name = ''

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
def first_day_declutter(arg):
    if stardew_valley.location_local == 'home' and stardew_valley.day_local == 1:
        print('You set down your bag. This is a new start, what name do you want to go by?')
        global player_name
        player_name = input('name:')
        print('Great, time to settle in for your first night (type sleep to sleep)')
        return
    else:
        return
def plots_check():
    print('These are your plots:')
    for key in stardew_valley.dictionary_of_plots_what_seed:
        print(str(key) + ': ' + stardew_valley.dictionary_of_plots_what_seed[key])
    print('And this is when they were planted:')
    for key in stardew_valley.dictionary_of_plots_grow_time:
        print(str(key) + ': ' + str(stardew_valley.dictionary_of_plots_grow_time[key]))

def trees_check():
    print('There are ' + str(stardew_valley.local_tree_count) + ' left')

def grass_check():
    print('Your grass is ' + stardew_valley.local_grass + ' to be cut')


location = 'farm'
town_loc = 'main'
wallet = 10
day = 1
daily_energy = 20
tree_count = 20
grass = 'ready'

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
        'wood': 0,
        'bass': 0,
        'trout': 0,
        'rainbow trout': 0,
    }
    dictionary_of_plots_grow_time = {
        1: 0,
        2: 0,
    }
    dictionary_of_plots_what_seed = {
        1: 'nothing',
        2: 'nothing'
    }
    dictionary_of_been_there_local = dictionary_of_been_there
    purchase_indicator = ''
    location_local = location
    town_loc_local = town_loc
    wallet_local = 10
    shopping_cart = 0
    are_buy = 0
    are_sell = 0
    inventory_indicator = 0
    day_local = day
    energy_local = daily_energy
    time = 1
    entered_home = 0
    local_tree_count = tree_count
    tree_regrowth = 0
    half_tree = 0
    local_grass = grass
    grass_grower = 0
    grass_notifier = 0
    beauty_index = 0

    def do_goto(self, arg):
        stardew_valley.are_sell = 0
        stardew_valley.are_buy = 0
        if arg == 'home':
            stardew_valley.location_local = arg
            stardew_valley.town_loc_local = 'main'
            goto_if_declutter(arg)
            first_day_declutter(arg)
            stardew_valley.entered_home = 1
            return
        else:
            pass
        if stardew_valley.entered_home != 0:
            pass
        else:
            print('You should probably check out your new home first')
            return
        if stardew_valley.day_local != 1:
            pass
        else:
            print('It is a bit late you should maybe go to sleep.')
            return
        if arg == 'farm'  or arg == 'town' or arg == 'lake':
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
            return



    def do_stock(self):
        if stardew_valley.location_local == 'store':
            pass
        else:
            print('You should go ask pierre what he sells')
            return
        print(dictionary_of_prices.keys())
        return

    def do_buy(self, arg):
        if stardew_valley.are_sell == 0:
            pass
        else:
            print('You are currently selling!')
            return
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
                stardew_valley.are_buy = 1
                return
            else:
                print(buy_error)
                return

    def do_amount(self, arg):
        if stardew_valley.are_sell == 0:
            pass
        else:
            print('please use num to tell me how many you want to sell')
            return
        if stardew_valley.are_buy == 1:
            pass
        else:
            print('You aren\'t buying anything!')
            return
        if int(arg) >= 0:
            pass
        else:
            print('You can\'t buy a negative amount silly!')
            return
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
                stardew_valley.are_buy = 0
                return
            else:
                print('You don\'t have enough money!')
                stardew_valley.are_buy = 0
                return
        else:
            print('The amount you buy needs to be a number!')
            stardew_valley.are_buy = 0
            return

    def do_sell(self, arg):
        if stardew_valley.are_buy == 0:
            pass
        else:
            print('You are currently buying!')
            return
        if stardew_valley.town_loc_local == 'store':
            pass
        else:
            print('You must be at the store to sell!')
            return
        if arg in dictionary_of_sell_prices:
            pass
        else:
            print('You can\'t sell that here!')
            return
        if stardew_valley.dictionary_of_inventory[arg] > 0:
            pass
        else:
            print('You don\'t have any to sell!')
            return
        stardew_valley.purchase_indicator = arg
        stardew_valley.are_sell = 1
        print('You want to sell ' + arg + '? I buy those for ' + str(dictionary_of_sell_prices[arg]) + '. How many do'
              + 'you want to sell? I buy them in bunches of ' +
              str(dictionary_of_quantity[stardew_valley.purchase_indicator]) + ' type \'num x\''
              )
        return

    def do_num(self, arg):
        if stardew_valley.are_sell == 1:
            pass
        else:
            print('I would like to know, what you want to sell first.')
            return
        if int(arg) >= 0:
            pass
        else:
            print('You can\'t sell a negative amount silly!')
            return
        if isinstance(int(arg), int):
            pass
        else:
            print('You need to type a number after num!')
            return
        if int(arg) * dictionary_of_quantity[stardew_valley.purchase_indicator] <= (
            stardew_valley.dictionary_of_inventory[stardew_valley.purchase_indicator]
                                                                                    ):
            pass
        else:
            print('You don\'t have that many to sell!')
            return
        stardew_valley.shopping_cart = int(arg) * dictionary_of_sell_prices[stardew_valley.purchase_indicator]
        stardew_valley.dictionary_of_inventory[stardew_valley.purchase_indicator] = (
            stardew_valley.dictionary_of_inventory[stardew_valley.purchase_indicator] -
            int(arg) * dictionary_of_quantity[stardew_valley.purchase_indicator]
        )
        stardew_valley.wallet_local = stardew_valley.wallet_local + stardew_valley.shopping_cart
        print('You sell ' + str(arg) + ' of' + stardew_valley.purchase_indicator + '!')
        print('You have ' + str(stardew_valley.dictionary_of_inventory[stardew_valley.purchase_indicator]) + ' left')
        stardew_valley.purchase_indicator = ''
        stardew_valley.shopping_cart = 0
        stardew_valley.are_sell = 0
        return

    def do_inventory(self, arg):
        for i in stardew_valley.dictionary_of_inventory:
            if stardew_valley.dictionary_of_inventory[i] == 0:
                pass
            else:
                stardew_valley.inventory_indicator += 1
                break
        if stardew_valley.inventory_indicator != 0:
            pass
        else:
            print('You aren\'t carrying anything right now')
        for key in stardew_valley.dictionary_of_inventory:
            if stardew_valley.dictionary_of_inventory[key] > 0:
                print(str(key) + ': ' + str(stardew_valley.dictionary_of_inventory[key]))
                break
            else:
                pass

    def do_wallet(self, arg):
        print('You have ' + str(stardew_valley.wallet_local) + ' coins right now')
        return

    def do_sleep(self, arg):
        if stardew_valley.location_local == 'home':
            pass
        else:
            print('You want to sleep in your bed')
            return
        if stardew_valley.local_grass == 'ready':
            pass
        else:
            if stardew_valley.grass_grower < 2:
                stardew_valley.grass_grower = stardew_valley.grass_grower + 1
            else:
                stardew_valley.grass_grower = 0
                stardew_valley.local_grass = 'ready'
                stardew_valley.grass_notifier = 1
        if stardew_valley.local_tree_count < 20:
            stardew_valley.local_tree_count = stardew_valley.local_tree_count + 1
            stardew_valley.tree_regrowth = stardew_valley.tree_regrowth + 1
        else:
            pass
        if stardew_valley.local_tree_count < 11:
            stardew_valley.local_tree_count = stardew_valley.local_tree_count + 4
            stardew_valley.tree_regrowth = stardew_valley.tree_regrowth + 4
        print('You go to bed')
        print('While you slept:')
        print(str(stardew_valley.tree_regrowth) + ' trees grew')
        if stardew_valley.grass_notifier == 0:
            pass
        else:
            print('Your grass is ready to cut')
            stardew_valley.grass_notifier = 0
        stardew_valley.time = 1
        stardew_valley.day_local = stardew_valley.day_local + 1
        return

    def do_check(self, arg):
        if stardew_valley.location_local == 'farm':
            pass
        else:
            print('You need to be at your farm to check')
            return
        if arg == 'plots':
            plots_check()
            return
        if arg == 'trees':
            trees_check()
            return
        if arg == 'grass':
            grass_check()
            return
        else:
            print('You cannot check that (maybe try inspect)')
            return

    def do_cut(self, arg):
        odd_tree = 0
        half_adder = 0
        if arg == 'trees':
            hours = input('How many hours would you like to cut? (it takes about two hours per tree)\nnumber:')
            if hours.isdigit():
                pass
            else:
                print('You need to input a number')
                return
            if int(hours) <= 16 - stardew_valley.time:
                pass
            else:
                print('you don\'t have that much time today you only have ' + str(16 - stardew_valley.time) +
                      ' hours left')
                return
            if int(hours) % 2 == 0:
                pass
            else:
                if stardew_valley.half_tree == 1:
                    half_adder = 1
                else:
                    stardew_valley.half_tree = 1
            trees = int(hours) / 2 + half_adder
            if trees <= stardew_valley.local_tree_count:
                pass
            else:
                trees_left = float(stardew_valley.local_tree_count) + .5 * float(odd_tree)
                new_trees = input('You will run out of trees before then, would you like to cut ' +
                                  str(stardew_valley.local_tree_count) + ' instead? \n(type y/n): ')
                if new_trees == 'y':
                    print('You cut down ' + str(stardew_valley.local_tree_count) + ' trees taking ' +
                          str(trees_left * 2) + ' hours')
                    stardew_valley.time = stardew_valley.time + trees_left * 2
                    stardew_valley.dictionary_of_inventory['wood'] = (stardew_valley.dictionary_of_inventory['wood']
                                                                      + stardew_valley.local_tree_count)
                    stardew_valley.local_tree_count = 0
                    return
                elif new_trees == 'n':
                    print('okay')
                    return
                else:
                    print('please type y or n')
                    return
            print('You cut down ' + str(trees) + ' trees taking ' + str(hours) + 'hours')
            stardew_valley.local_tree_count = stardew_valley.local_tree_count - trees
            stardew_valley.time = stardew_valley.time + int(hours)
            stardew_valley.dictionary_of_inventory['wood'] = stardew_valley.dictionary_of_inventory['wood'] + int(trees)
            print('There are ' + str(stardew_valley.local_tree_count) + ' remaining')
            return
        elif arg == 'grass':
            if stardew_valley.time <= 13:
                pass
            else:
                print('you don\'t have enought time to cut grass')
                return
            if stardew_valley.local_grass == 'ready':
                print('you cut the grass, it takes 2 hours and you get 2 hay')
                stardew_valley.local_grass = 'not ready'
            else:
                print('the grass is already cut')
                return
        else:
            print('You can\'t cut that')
            return

    def do_fish(self, arg):
        if stardew_valley.location_local == 'lake':
            pass
        else:
            print('There is no-where to fish here')
            return
        fish_time = input('How many hours would you like to fish? : ')
        fish_weight = int(fish_time) / 2
        allowed_pull = int(fish_time) * 3
        power_switch = 1
        beauty = 0
        while power_switch == 1:
            if beauty % 7 != 0:
                pass
            else:
                if stardew_valley.beauty_index < 4:
                    pass
                else:
                    stardew_valley.beauty_index = 0
                print(dictionary_of_beauty[stardew_valley.beauty_index])
                stardew_valley.beauty_index += 1
            fish_catcher = random.randrange(100)
            fish_obtain = fish_catcher / fish_weight
            pull_count = 0
            s = input('pull? :')
            if s != 'pull':
                stardew_valley.time = stardew_valley.time + int(fish_time)
                return
            else:
                if pull_count <= allowed_pull:
                    pass
                else:
                    print('you finish fishing')
                    stardew_valley.time = stardew_valley.time + int(fish_time)
                if fish_obtain > dictionary_of_fishing['trout']:
                    print('You caught some garbage')
                    beauty += 1
                elif fish_obtain > dictionary_of_fishing['rainbow_trout']:
                    print('you caught a trout!')
                    stardew_valley.dictionary_of_inventory['trout'] += 1
                    beauty += 1
                elif fish_obtain > dictionary_of_fishing['bass']:
                    print('you caught a rainbow-trout!')
                    stardew_valley.dictionary_of_inventory['rainbow trout'] += 1
                    beauty += 1
                else:
                    print('You caught a bass!')
                    stardew_valley.dictionary_of_inventory['bass'] += 1
                    beauty += 1




if __name__ == "__main__":
    stardew_valley().cmdloop()
