#  Shell
import random 

n = 5
arr = list()
for i in range(n):
    chis = random.randint(1,100)
    arr.append(chis)

print('Not sorted: ')
print(arr)
print('------')

step = len(arr) // 2
while step > 0:
    for i in range(step,  n, 1):
        value = arr[i]
        current_index = i
        index_to_check = current_index - step
        while current_index > 0 and arr[index_to_check] > value:
           arr[current_index] = arr[index_to_check]
           current_index -= step
           index_to_check -= step
        arr[current_index] = value
    step = step // 2

print('Sorted: ')
print(arr)

# Фрагмент кода использует алгоритм сортировки оболочки, средняя временная сложность которого составляет O(n ^ 2).
# Внешний цикл while выполняет итерацию log(n) раз, где n - длина массива. В рамках каждой итерации внутренний цикл for повторяется n / 2 раза. Следовательно, общая временная сложность равна O(n ^2).	