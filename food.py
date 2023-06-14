my_food = ['pizza', 'falafel', 'ciasto z marchwi']
friend_food = my_food[:]

my_food.append('kiełbasa z grilla')
friend_food.append('lody')

print("Moje ulubione potrawy to:")
print(my_food)

print('\nUlubione potrawy mojego przyjaciela to:')
print(friend_food)

print('Pierwsze trzy elementy listy to:')
print(my_food[:3])

print('Środkowe trzy elementy listy to:')
print(my_food[1:4])

print('Ostatnie trzy elementy listy to:')
print(my_food[1:])