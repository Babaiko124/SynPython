# Задание 1
n=int(input("Введите количество элементов списка "))
res = []
for i in range(n):
    a = int(input('Введите значение '))
    res.append(a)
res.reverse()
print(*res)

# Задание 2
n=int(input('Введите число '))
res=list(map(int,input('Введите числа через пробел').split()))[:n]
res.insert(0,res.pop())
print(res)

# Задание 3
m = int(input('Максимальная масса перевозки '))
n = int(input('Количество рыбаков '))
fishermen = []
for i in range(n):
    ai = int(input('Масса рыбака '))
    if 1 <= ai <= m:
        fishermen.append(ai)
fishermen.sort()
boats_count = 0
i = 0
while i < n:
    if i + 1 < n and fishermen[i] + fishermen[i+1] <= m:
        i += 2
    else:
        i += 1
    boats_count += 1
print(boats_count)