alien_color = "zielony"
if alien_color == "zielony":
    print("zarobiłeś 5 pkt")
elif alien_color == "zółty":
    print('zarobiłeś 10 pkt')
else:
    print('zarobiłeś 15 pkt')

age = 21
if age <= 2:
    print("jesteś niemowlęciem")
elif age >2 and age <= 4:
    print('uczysz się  chodzić')
elif age >4 and age <= 13:
    print('jesteś dzieckiem')
elif age >13 and age <= 20:
    print('jesteś nastolatkiem')
elif age >20 and age <= 65:
    print('jesteś dorosłym')
else:
    print('jesteś seniorem')


owoce = ['banany', 'jabłka', 'gruszki']
if "banany" in owoce:
    print('naprawde lubisz banany')
if "jabłka" in owoce:
    print('naprawde lubisz jabłka')
if "śliwki" in owoce:
    print('nie lubisz śliwek')