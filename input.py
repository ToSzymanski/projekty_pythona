#message = input("wpisz swoje imie:")
#print(message)


#car = input("Jaki samochód chcesz wypozyczyć?")
#print(f'Chwileczkę, spawdzam czy samochód {car} jest dostępny')

#table = input('Dla ilu osób chcesz zarezwerować stolik?')
#table = int(table)

#if table > 8:
#    print("musisz poczekać na stolik")
#else:
#    print("Twój stolik jest gotowy")

number = input('Podwaj dowolną liczbę:')
number = int(number)

if number % 10 == 0:
    print("Twoja liczba to wielokrotność 10")
else:
    print("Twoja liczba nie jest wielokrotnością 10")