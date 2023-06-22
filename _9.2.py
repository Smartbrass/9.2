a = input('Введите числа через пробел:')
b = input('Введите числа через пробел:')
a1 = [int(_) for _ in a.split()]
b1 = [int(_) for _ in b.split()]
print(len(a1))
print(len(b1))
print('Одновременно чисел в списках:', len(a1) + len(b1))