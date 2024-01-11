#  Быстрая сортировка
import random 

n = 10
arr = list()
for i in range(n):
    chis = random.randint(1,100)
    arr.append(chis)

print('Not sorted: ')
print(arr)
print('------')

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    index_of_strong_elem = random.randint(0, len(arr))
    strong_elem = arr[index_of_strong_elem]
    low = list()
    mid = list()
    high = list()

    for elem in arr:
        if elem == strong_elem:
            mid.append(elem)
        elif elem < strong_elem:
            low.append(elem)
        else:
            high.append(elem)

    low = quick_sort(low)
    high = quick_sort(high)
    result = low + mid + high
    return result

arr = quick_sort(arr)
print('Sorted: ')
print(arr)



# В худшем случае алгоритм выполнит n рекурсивных вызовов, каждый раз разбивая массив на две половины.
# Этап разделения занимает O (n) времени, и поскольку он выполняется рекурсивно, общая временная сложность составляет O (n log n).