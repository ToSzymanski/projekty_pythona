lista_gosci = ["Bill Gates", "Steave Jobs", "Albert Einstein"]
print(f'Na obiad zostalo zaproszonych {len(lista_gosci)} gosci')
print(f'Chętnie zaproszę na obiad {lista_gosci[1]}, {lista_gosci[0]}, {lista_gosci[2]}')
nieobecny = lista_gosci.pop(0)
print(f'Niestety na obiad nie moze przyjś przyjśc {nieobecny}')
nowy_zaproszony = lista_gosci.insert(1,"Paul Anka")
print(f'Nowe zaproszenie kieruje do {lista_gosci[1]}, {lista_gosci[0]}, {lista_gosci[2]} ')

print('Znalazlem wiekszy stól i moge zaprosic jeszcze 3 gosci')
lista_gosci.insert(0, "Tomek")
lista_gosci.insert(2, "Marcin")
lista_gosci.append("Piotrek")

print(f'Nowa lista zaproszonych gości to {lista_gosci}')
print(f'Na obiad zostalo zaproszonych {len(lista_gosci)} gosci')
print("stolu wiekszego jednak nie będzie i moge zaprosic tylko 2 gosci")

niemozliwy_do_zaproszenia = lista_gosci.pop()
print(f'{niemozliwy_do_zaproszenia} przepraszam ale nie moge Ciebie zaprosic')

niemozliwy_do_zaproszenia = lista_gosci.pop()
print(f'{niemozliwy_do_zaproszenia} przepraszam ale nie moge Ciebie zaprosic')

niemozliwy_do_zaproszenia = lista_gosci.pop()
print(f'{niemozliwy_do_zaproszenia} przepraszam ale nie moge Ciebie zaprosic')

niemozliwy_do_zaproszenia = lista_gosci.pop()
print(f'{niemozliwy_do_zaproszenia} przepraszam ale nie moge Ciebie zaprosic')

print(lista_gosci)
print(f"{lista_gosci[0]}, {lista_gosci[1]} ciągle zapraszam Was na obiad")


del lista_gosci[1]
del lista_gosci[0]

print(lista_gosci)

print(f'Na obiad zostalo zaproszonych {len(lista_gosci)} gosci')