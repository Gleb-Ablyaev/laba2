import numpy as np
from numpy import linalg

size = int(input('Введите размерность квадратной матрицы больше 1 и меньше 31:'))
while (size < 1) or (size > 31):
    size = int(input("Вы ввели неверное число. "
                  "\nВведите количество строк (столбцов) квадратной матрицы больше 1 и меньше 31:"))
mat = np.random.randint(5, size=(size, size))
r = np.linalg.matrix_rank(mat)
print("Матрица:\n", mat)
print("Ранг матрицы:", r)
t = int(input('Введите количество знаков после запятой в результате вычисления:'))
t = 0.1 ** t
n = 1
fact = 1
summ = 0
flg = 0
raz = 1
while abs(raz) > t:
    flg += summ
    summ += (np.linalg.det(linalg.matrix_power(mat, n))) / fact
    n += 1
    fact = fact * n * (n - 1)
    raz = abs(flg-summ)
    flg = 0
    print(n-1, ':', summ, ' ', raz)
print('Сумма знакопеременного ряда:', summ)