favorite_places = {
    'jola' : ['wlochy', 'hiszpania', 'izrael'],
    'tomek' : ['gruzja', 'wlochy', 'hiszpania'],
    'stefan' : ['hiszpania', 'grecja', 'turcja'],
    }

for user, places in favorite_places.items():
    print(f'Dla {user.title()} ulubione miejsca to:')
    for place in places:
        print(f'\t{place.title()}')
    print('\n')