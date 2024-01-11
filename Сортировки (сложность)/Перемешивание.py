#  Сортировка перемешиванием
import random 

n = 5
arr = list()
for i in range(n):
    chis = random.randint(1,100)
    arr.append(chis)

print('Not sorted: ')
print(arr)
print('------')

left_index = 0
right_index = n - 1
is_sorted = True
while left_index <= right_index:
    for i in range(left_index, right_index, +1):
        left = arr[i]
        right = arr[i + 1]
        if left < right:
            is_sorted = False
            arr[i] = right
            arr[i + 1] = left
    right_index = right_index - 1
    for i in range(right_index, left_index, -1):
        right = arr[i]
        left = arr[i - 1]
        if left < right:
            is_sorted = False
            arr[i] = left
            arr[i - 1] = right
    left_index += 1
    print(arr)
    if is_sorted is True:
        break
    else:
        is_sorted = True
     
print('Sorted: ')
print(arr)


# Фрагмент кода использует алгоритм пузырьковой сортировки для сортировки списка 'arr'.
# Внешний цикл while выполняется в течение 'n' итераций, где 'n' - длина списка.
# Внутренние циклы for выполняются по 'n-1' итерациям каждый, в результате чего получается в общей сложности (n-1) + (n-2) + ... + 1 = n(n-1)/ 2 итерации. Следовательно, общая временная сложность равна O(n^2).