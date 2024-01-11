#  Сортировка выбором
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
    min_max_index = i
    for j in range(i + 1, n, +1):
        if arr[j] > arr[min_max_index]:
            min_max_index = j
    temp = arr[i]
    arr[i] = arr[min_max_index]
    arr[min_max_index] = temp
    print(arr)



print('Sorted: ')
print(arr)

# Фрагмент кода использует вложенный цикл для выполнения сортировки выделений.
# Внешний цикл повторяется n раз, а внутренний цикл повторяется n-1, n-2, ..., 1 раз соответственно. Следовательно, общее количество итераций составляет приблизительно n*(n-1)/2, что соответствует порядку O(n^2).Ы