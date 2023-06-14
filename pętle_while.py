prompt = "Podaj swój ulubiony dodatek do pizzy"
prompt += "\njeśli nie masz juz wiecej ulubionych dodatków do pizzy wpisz 'koniec':"

flag = True

while flag:
    message = input(prompt)
    if message == 'koniec':
        flag = False
    else:
        print(f'dodaje {message} do Twojej pizzy')
