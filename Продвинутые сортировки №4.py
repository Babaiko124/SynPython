def step(n):
    return str(n) if n < 2 else step(n // 2) + str(n % 2)

def mult(x, y):
    if y == 0:
        return 0
    elif y > 0:
        return x + mult(x, y - 1)
    else:
        return -mult(x, -y)

def de(num, exp):
    if exp == 0:
        return 1
    elif num > 0:
        return num * de(num, exp - 1)
    else:
        return 1 / de(num, -exp)

print('*** Функция перевода числа в двоичную систему ***')
n = int(input('Введите число: '))
print(step(n))

print('*** Функция умножения чисел ***')
x= int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
print(mult(x, y))

print('*** Функция возведения чисел в степень ***')
num= int(input('Введите число: '))
exp = int(input('Введите степень: '))
print(de(num, exp))