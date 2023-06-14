my_pizzas = ['margerita', 'capriciosa', 'hawajska', 'wiejska']
friend_pizzas = my_pizzas[:]

my_pizzas.append('rzymska')
friend_pizzas.append('napolitańska')

print("Moje ulubione pizze to:\n")
for my_pizza in my_pizzas:
    print(my_pizza)

print('\nUlubione rodzaje pizzy mojego przyjaciela to:\n')
for friend_pizza in friend_pizzas:
    print(friend_pizza)