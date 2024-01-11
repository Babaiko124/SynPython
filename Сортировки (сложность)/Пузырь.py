#  Сортировка пузырьком
import random 

n = 5
arr = list()
for i in range(n):
    chis = random.randint(1,100)
    arr.append(chis)

print('Not sorted: ')
print(arr)
print('------')

for i in range(n):
    for j in range(n-1):
        left = arr[j]
        right = arr[j + 1]
        if left > right:
            arr[j] = right
            arr[j + 1] = left

print('Sorted: ')
print(arr)

# Фрагмент кода содержит вложенный цикл. Внешний цикл выполняется n раз, а внутренний цикл выполняется n-1 раз для каждой итерации внешнего цикла.
# Следовательно, общее количество итераций равно n * (n-1), что упрощается до O (n ^ 2) в нотации Big O.