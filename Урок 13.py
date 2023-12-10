# Задание 1
import random
l = int(input('Введите длину матрицы: '))
h = int(input('Введите высоту матрицы: '))
a = int(input('Введите начальное значение диапазона генерации матрицы: '))
b = int(input('Введите конечное значение диапазона генерации матрицы: '))
matrix_1=[[random.randint(a,b) for j in range(h)] for i in range(l)]
print('Матрица 1: ')
for i in range(l):
    print(matrix_1[i])
matrix_2 = [[random.randint(a,b) for j in range(h)] for i in range(l)]
print('Матрица 2: ')
for i in range(l):
    print(matrix_2[i])
result = [[matrix_1[i][j] + matrix_2[i][j] for j in range(len(matrix_1[0]))] for i in range(len(matrix_1))]
print("Результат сложения двух матриц: ")
for r in result:
    print(r)
