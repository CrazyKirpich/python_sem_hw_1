# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y)

numberQ = int(input('Введите номер четверти: '))
if 0 < numberQ < 5:
    if numberQ == 1:
        print(f'X > 0; Y > 0')
    elif numberQ == 2:
        print(f'X < 0; Y > 0')
    elif numberQ == 3:
        print(f'X < 0; Y < 0')
    else:
        print(f'X > 0; Y < 0')
else:
    print('Четвертей четыре')
