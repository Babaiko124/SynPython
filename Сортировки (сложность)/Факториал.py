fib1 = fib2 = 1
print(fib1,fib2, end=' ')
n = 5
for i in range(2, n):
    summa = fib2 + fib1
    fib1 = fib2
    fib2 = summa
    print(summa, end = ' ')

    # Фрагмент кода содержит цикл for, который повторяется от 2 до n, поэтому количество итераций прямо пропорционально значению n.
    # Внутри цикла выполняются операции с постоянным временем, такие как сложение и присваивание. Следовательно, общая временная сложность кода равна O(n).