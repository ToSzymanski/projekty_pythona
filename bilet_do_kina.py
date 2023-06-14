prompt = "wpisz swój wiek:"
prompt += "\n jeśli chcesz zakończyć program wpisz 'koniec'"
message = "Cena biletu dla Ciebie to:"
flag = True
while flag:
    age = input(prompt)
    if age == 'koniec':
        break
    age = int(age)
    if age < 3:
        print(f'{message} 4 zł')
    elif age > 3 and age <= 12:
        print(f'{message} 10 zł')
    else:
        print(f'{message} 15 zł')


