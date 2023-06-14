
user = {
    'first_name' : 'jola',
    'last_name' : 'szymanska',
    'age' : 35,
    'location' : 'Warszawa',
    }

print(user['first_name'])
print(user)


friends_number = {
    'jola' : 7,
    'tomek' : 9,
    'robert' : 12,
    'stefan' : 13,
    'adam' : 24,
    }

for friend, number in friends_number.items():
    print(f'Ulubiona liczba {friend.title()} to {number}')