# Задание 1
pets ={}
pets2={}
for i in range(1):
    k=input("Введите имя питомца : ")
    if k=='':
        break
    else:
        k1=input('Вид питомца: ')
        k2=int(input('Возраст питомца: '))
        k3=input('Имя владельца:  ')
        pets2={'Вид питомца:':k1, 'Возраст питомца:':k2, 'Имя владельца:':k3  }
        pets[k]=pets2
        for key, value in pets.items():
            v=value['Вид питомца:']
            vz=value['Возраст питомца:']
            name=value['Имя владельца:']
            year = ''
            if vz % 10 == 1 and vz != 11 and vz % 100 != 11:
                year = 'год'
            elif 1 < vz % 10 <= 4 and vz != 12 and vz != 13 and vz != 14:
                year = 'года'
            else:
                year = 'лет'
print("Это", v, "по кличке",f'"{key}"',". Возраст питомца:", vz,year,'.', "Имя владельца:", name)

# Задание 2
step = {}
a=int(input('Начальное значение '))
b=int(input('Конечное значение '))
c=int(input('Шаг '))
for i in range(a, b,c):
    step[i] = i ** i
print(step)
