numbers = []
for number in range(1,10):
    numbers.append(number)

for number in numbers:
    if number == 1:
        print(f'{number}st')
    if number == 2:
        print(f'{number}nd')
    if number == 3:
        print(f'{number}rd')
    if number >= 4:
        print(f'{number}th')