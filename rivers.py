country_river = {'egipt' : 'nil', 'polska' : 'wisła', 'austria' : 'dunaj'}

for country, river in country_river.items():
    print(f'{river.title()} to rzeka która przepływa przez {country.title()}')

for river in country_river.values():
    print(river)

for country in country_river.keys():
    print(country)