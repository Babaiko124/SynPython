#  Сортировка слиянием
import random 

n = 10
arr = list()
for i in range(n):
    chis = random.randint(1,100)
    arr.append(chis)

print('Not sorted: ')
print(arr)
print('------')

def merge(arrr,arrl):
     sorted_arr = list()
     c_left = 0
     c_right = 0
     lenl = len(arrl)
     lenr = len(arrr)
     for i in range(lenl + lenr):
          if c_left < lenl and c_right < lenr:
            if arrl[c_left] < arrr[c_right]:
                sorted_arr.append(arrl[c_left])
                c_left += 1
            else:
                sorted_arr.append(arrr[c_right])
                c_right += 1
          else:
              if c_left == lenl:
                  for j in range(c_right, lenr):
                      sorted_arr.append(arrr[j])
              else:
                  for j in range(c_left, lenl):
                      sorted_arr.append(arrl[j])
              break
     return sorted_arr
               
     
      
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = list()
    right = list()
    
    for i in range(0, mid):
        val = arr[i]
        left.append(val)
    
    for i in range(mid, len(arr)):
            val = arr[i]
            right.append(val)
    
    left = merge_sort(left)
    right = merge_sort(right)
    result = merge(left,right)
    return result

arr = merge_sort(arr)
print('Sorted: ')
print(arr)



# В функции merge_sort массив рекурсивно делится на две половины до тех пор, пока не будет достигнут базовый вариант (когда длина массива меньше или равна 1). 
# Этот процесс разделения занимает O (log n) времени. Затем вызывается функция merge для объединения разделенных массивов, что занимает O (n) времени.
# Поскольку функция merge_sort вызывается рекурсивно для каждой половины массива, общая временная сложность алгоритма сортировки слиянием равна O(n log n).