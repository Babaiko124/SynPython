# Задание 1
a = int(input("Введите целое число "))
if a==0:
    print('Это нулевое число.')
elif a%2==1 and a>0:
    print('Это положительное нечетное число.')
elif a%2==0 and a>0:
    print('Это положительное четное число.')
elif a%2==1 and a<0:
    print('Это отрицательное нечетное число.')
elif a%2==0 and a<0:
    print('Это отрицательное четное число.') 
 
# Задание 2
slovo = input('Введите слово: ')
sa=slovo.count('a') 
se=slovo.count('e') 
si=slovo.count('i') 
so=slovo.count('o') 
su=slovo.count('u') 
glas=sa+se+si+so+su 
print("Всего гласных: ",glas) 
print("Всего согласных: ",len(slovo)-glas)
if sa==0:
    print ("False")
else:
    print("a =",sa)
if si==0:
    print ("False")
else:
    print("i =",si)
if se==0:
    print ("False")
else:
    print("e =",se)
if so==0:
    print ("False")
else:
    print("o =",so)
if su==0:
    print ("False")
else:
    print("u=",su)

# Задание 3
smin=int(input("Минимальная сумма инвестиций: "))
m=int(input("Cколько $ у Майкла: "))
i=int(input("Сколько $ у Ивана: "))
if m>=smin and i>=smin:
    print(2)
elif m>=smin and i<=smin:
    print("Mike")
elif m<=smin and i>=smin:
    print("Ivan")
elif m<=smin and i<=smin and (m+i)>=smin:
    print(1)
elif m<=smin and i<=smin and (m+i)<=smin:
    print(0)