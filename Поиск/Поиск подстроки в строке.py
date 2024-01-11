# Поиск подстроки в строке

str_where = 'hello world'
str_find = ' wor'

index_where = 0
index_find = 0
len_where = len(str_where)
len_find = len(str_find)

while (index_where <= len_where - len_find and
        index_find < len_find):
    if str_where[index_where + index_find] == str_find[index_find]:
        index_find += 1
    else:
        index_where += 1
        index_find = 0

print(str_where)
print(str_find)

if index_find == len_find:
    print(f'Такая подстрока есть. Её начало тут - {index_where}')
else:
    print(f'Такой подстроки нет.')
