m=int(input('Максимальная масса перевозки '))
n=int(input('Количество рыбаков '))
ship=[]
for i in range(n):
    ai=int(input('Масса рыбака '))
    if 1<=ai<=m:
        ship.append(ai)
print(len(ship))