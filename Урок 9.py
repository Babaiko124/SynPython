# Задание 1
a=int(input('Введите количество чисел '))
chis=list(map(int,input('Введите числа через пробел ').split()))[:a]
razn=set(chis)
print(len(razn))

# Задание 2
a=set(input('Введите числа в первый список через пробел ').split())
b=set(input('Введите числа во второй список через пробел ').split())
print(len(a.intersection(b)))

# Задание 3
chis=set()
a=input('Введите последовательность чисел через пробел ').split()
for i in a:
    if i in chis:
        print('YES')
    else:
        chis.add(i)
        print('NO')