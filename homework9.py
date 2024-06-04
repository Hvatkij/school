print('Введите три целых числа: ')
first, second, third = input().split()
first, second, third = int(first), int(second), int(third)  # как то вводят сразу int но .split
if first == second and second == third and first == third:  #  тут начинается индийский код. я пропал.
    print(3)
elif first == second and first != third\
        or first == third and first != second\
        or second == third and second != first:
    print(2)
else:
    print(0)