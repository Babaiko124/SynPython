# Задание 1
m = input('Введите данные ')
if m == m[::-1]:
    print('Yes')
else:
    print('No')

# Задание 2
string=input('Введите строку')[:1000]
strip=' '.join(string.split())
print(strip)