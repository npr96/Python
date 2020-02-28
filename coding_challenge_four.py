import cmd, sys

dictionary_of_sales = {
    'google' : 15,
    'facebook' : 20,
    'twitter' : 8,
    'offline' : 12
}
sales_dictionary = dictionary_of_sales.copy()
changer_value = ''
changer = ''
class histogram(cmd.Cmd):
    intro = 'Welcome to histogram, type help for a list of commands'
    prompt = '-H-'
    file = None
    def do_print(self, arg):
        print('g ' + '$' * sales_dictionary['google'])
        print('f ' + '$' * sales_dictionary['facebook'])
        print('t ' + '$' * sales_dictionary['twitter'])
        print('o ' + '$' * sales_dictionary['offline'])    
    def do_change(self, arg):
        global changer
        if arg == 'google':
            print('how much would you like to change it?')
            changer = 'google'
            return
        if arg == 'facebook':
            print('how much would you like to change it?')
            changer = "facebook"
            return
        if arg == 'twitter':
            print('how much would you like to change it?')
            changer = 'twitter'
            return
        if arg == 'offline':
            print('how much would you like to change it?')
            changer = "offline"
            return
        else:
            print('that is not a company you can change')
            return
    def do_amount(self, arg):
        global sales_dictionary
        change_magnitude = int(arg)
        sales_dictionary[changer] = dictionary_of_sales[changer] + change_magnitude
    def do_changer(self, arg):
        print(changer)

if __name__ == "__main__":
    histogram().cmdloop()