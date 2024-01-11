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
        left = arr[j]
        right = arr[j+1]
        if left > right:
            is_sorted = False
            arr[j] = right
            arr[j+1] = left
    if is_sorted is True:
        break
    else:
        is_sorted = True
            

print('Сортировано:')
print(arr)