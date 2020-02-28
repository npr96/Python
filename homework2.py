filter_genre = {
    'action' :  {'HBO' : {'Show1' : 'The Pacific',
                         'Show2' : 'Watchmen',},
                'TNT' : {'Show1' : 'Top Gun',
                         'Show2' : 'Terminator'}},
    'romance' : {'ABC' : {'Show1' : 'The Bachelorette',
                         'Show2' : 'Once Upon a Time'},
                'CBS' : {'Show1' : 'Mom',
                         'Show2' : 'I Love Lucy'}},
    'comedy' :  {'Fox' : {'Show1' : 'How I Met Your Mother',
                         'Show2' : 'New Girl'},
                'DSN' : {'Show1' : 'That\'s so Raven',
                         'Show2' : 'Mickey\'s Playhouse'}}
}
print(filter_genre.keys())
print(filter_genre['comedy'].keys())
print(filter_genre['romance'].items())
print(filter_genre['action']['HBO']['Show2'])