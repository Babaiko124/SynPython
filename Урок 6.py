# Задание 1
n=int(input("Введите количество чисел "))
a=0
for i in range(1, n+1):
    s=int(input("Введите целое число "))
    if s==0:
        a+=1
print(a)

# Задание 2
x=int(input('Введите натуральное число '))
a=0
for b in range(1, x+1):
    if x%b==0:
        a=a+1
print(a)

# задание 3
a=int(input())
b=int(input())
for i in range(a, b + 1):
    if i % 2 == 0:
        print(i, end=' ')