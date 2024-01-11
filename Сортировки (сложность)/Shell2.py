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
        current_index = i
        index_to_check = current_index - step
        while current_index > 0 and arr[index_to_check] > arr[current_index]:
           temp = arr[current_index]
           arr[current_index] = arr[index_to_check]
           arr[index_to_check] = temp
           current_index -= step
           index_to_check -= step
           step = step // 2

print('Sorted: ')
print(arr)

# Временная сложность этого алгоритма равна O (n ^ 2) в наихудшем случае.
# Это связано с тем, что алгоритм использует вложенные циклы для сравнения и замены элементов местами, а количество итераций в каждом цикле пропорционально размеру входного массива.
# Пространственная сложность этого алгоритма равна O (1), потому что он не использует никаких дополнительных структур данных, которые растут с размером входных данных.
# Сортировка выполняется на месте, что означает, что исходный массив изменяется напрямую.