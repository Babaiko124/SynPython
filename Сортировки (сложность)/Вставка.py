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
    val = arr[i]
    j = i - 1
    while val < arr[j] and j >= 0:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = val
    print(arr)

print('Sorted: ')
print(arr)

# Фрагмент кода использует алгоритм сортировки по вставке для сортировки данного массива.
# В наихудшем сценарии, когда массив находится в обратном порядке, цикл while внутри цикла for будет повторяться n-1 раз для каждого элемента в массиве. Следовательно, общая временная сложность кода равна O(n ^2).