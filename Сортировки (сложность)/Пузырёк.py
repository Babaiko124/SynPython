import random

n = 10
arr = list()
for i in range(n):
    number = random.randint(1,100)
    arr.append(number)

print('Не сортировано:')
print(arr)
print('------')

is_sorted = True

for i in range(n):
    for j in range(n-1-i):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp
            

print('Сортировано:')
print(arr)

# n*(n-1) = n^2 - n 
# O(n^2) - используется 2 цикла for