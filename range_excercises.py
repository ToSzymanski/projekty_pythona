#for value in range(1,21):
#    print(value)
    
    
lista_milion = []
for liczba in range(1,1000001):
    lista_milion.append(liczba)
    
wartosc_min = min(lista_milion)
wartość_max = max(lista_milion)
suma_listy = sum(lista_milion)
print(wartość_max)
print(wartosc_min)
print(suma_listy)


liczby_nieparzyste = []
for nieparzysta in range(1,21,2):
    liczby_nieparzyste.append(nieparzysta)
    print(liczby_nieparzyste)

lista_trzy = [value**3 for value in range(3,31)]
print(lista_trzy)

szesciany = [szescian**3 for szescian in range(1,11)]
print(szesciany)

