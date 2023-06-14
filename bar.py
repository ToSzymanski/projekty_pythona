sandwitch_orders = ['kanapka z pastrami', 'kanapka z tuńczykiem', 'kanapka z bekonem', 'kanapka z pastrami', 'kanapka z jajkiem', 'kanapka z szynką', 'kanapka z pastrami',]
finished_sandwiches = []
print('W barze skończyło się pastrami')

# print(sandwitch_orders)
# usuwanie kanapek których nie mozna zrobić
while 'kanapka z pastrami' in sandwitch_orders:
    sandwitch_orders.remove('kanapka z pastrami')
print(sandwitch_orders)
# przygotowanie zamówień które mozna zrobic
while len(sandwitch_orders) != 0:
    
    order = sandwitch_orders.pop()
    finished_sandwiches.append(order)
    print(f'Przygotowano {order}')
#weryfikacja list zamówień
print(sandwitch_orders)
print(finished_sandwiches)