#### 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
#### и проверяет, является ли этот день выходным.

# day = int(input('Введите день недели...  '))
# if day > 0 and day < 6:
#     print(day, '<= этот день является рабочим днём')
# elif day > 5 and day < 8:
#     print(day, '<= этот день является выходным днём')
# else:
#     print(day, '<= это значение не является днём недели')

#### 2. Напишите программу для проверки истинности утверждения 
#### ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
#### Г = not ; V = or ; ^ = and

# X = 0
# Y = 0
# Z = 0
# rang = range(0, 2)
# for X in rang:
#     for Y in rang:
#         for Z in rang:
#             print(not (X or Y or Z) == (not X and not Y and not Z), end=' = ')
#             print(X, Y, Z)

#### 3. Напишите программу, которая принимает на вход координаты точки (X и Y), 
#### причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка 
#### (или на какой оси она находится).

# X = int(input('Введите координату X...  '))
# Y = int(input('Введите координату Y...  '))

# if X > 0 and Y > 0:
#     print('Точка', (X, Y), 'находится в Первой четверти')
# elif X > 0 and Y < 0:
#     print('Точка', (X, Y), 'находится во Второй четверти')
# elif X < 0 and Y < 0:
#     print('Точка', (X, Y), 'находится в Третьей четверти')
# elif X < 0 and Y > 0:
#     print('Точка', (X, Y), 'находится в Четвёртой четверти')
# elif X == 0 and Y != 0:
#     print('Точка', (X, Y), 'лежит на оси X')
# elif X != 0 and Y == 0:
#     print('Точка', (X, Y), 'лежит на оси Y')
# else:
#     print('Обе точки не могут быть равны нулю!')

#### 4. Напишите программу, которая по заданному номеру четверти, 
#### показывает диапазон возможных координат точек в этой четверти (x и y).

# Axis = int(input('Введите номер четверти...  '))

# if Axis == 1:
#    print('Список значений соответствующих номеру четверти = ', Axis)
#    for X in range(1, 10):
#     for Y in range(1,10):
#         print((X, Y), end='--')
# elif Axis == 2:
#    print('Список значений соответствующих номеру четверти = ', Axis)
#    for X in range(1, 10):
#     for Y in range(-10, -1):
#         print((X, Y), end='--')
# elif Axis == 3:
#    print('Список значений соответствующих номеру четверти = ', Axis)
#    for X in range(-10, -1):
#     for Y in range(-10, -1):
#         print((X, Y), end='--')
# elif Axis == 4:
#    print('Список значений соответствующих номеру четверти = ', Axis)
#    for X in range(-10, -1):
#     for Y in range(1,10):
#         print((X, Y), end='--')
# else:
#    print('Данное значение не соответствует номеру четверти')

#### 5. Напишите программу, которая принимает на вход координаты двух точек 
#### и находит расстояние между ними в 2D пространстве.

# A = int(input('Введите координату X для первой точки...')), int(input('Введите координату Y для первой точки...'))
# B = int(input('Введите координату X для второй точки...')), int(input('Введите координату Y для второй точки...'))

# distance = round(((B[0] - A[0]) ** 2 + (B[1] - A[1]) ** 2) ** 0.5, 2)
# print('Расстояние между точками ',A ,' и ',B, 'равняется',  distance)