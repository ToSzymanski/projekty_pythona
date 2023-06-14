"""
users = ['admin', 'eryk', 'marcin', 'tomek', 'janek']
if users:
    for user in users:
        if user == 'admin':
            print(f'witaj {user.title()}, czy chcesz przejrzeć raport')
        else:
            print(f'Witaj {user.title()} Super ze ponownie się zalogowałeś')
else:
    print('Trzeba dodać jakiś uzytkowników serwisu')
"""

current_users = ['tomek', 'wojtek', 'janek', 'jola', 'piotrek']
current_users_lowercase = []

for current_user in current_users:
    current_users_lowercase.append(current_user.lower())
print(current_users_lowercase)
new_users = ['Tomek', 'STEfan', 'ula', 'janek']
new_users_lowercase = []
for new_user in new_users:
    new_users_lowercase.append(new_user.lower())
print(new_users_lowercase)
for new_user_lowercase in new_users_lowercase:
    if new_user_lowercase in current_users_lowercase:
        print(f"{new_user_lowercase.title()} Twoja nazwa uzytkownika jest juz zajęta")
    else:
        print(f"{new_user_lowercase.title()} Twoja nazwa jest dostępna")