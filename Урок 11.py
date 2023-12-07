# Задание 1
def fac(a):
    if a == 0:
        return 1
    return fac(a-1)*a

spis = []
s=int(input('Введите число: '))
for i in range(s,0,-1):
    spis.append(fac(i))
print(spis)

# Задание 2
import collections
pets = {
    1:{
"Мухтар": {
"Вид": "Собака",
"Возраст": 9,
"Имя владельца": "Павел"},
},
2:{
"Каа": {
"Вид": "желторотый питон",
"Возраст": 14,
"Имя владельца": "Саша"},
},
}

def get_pet(ID):
    return pets.get(ID, False)

def get_suffix(age):
    if age % 10 == 1 and age != 11 and age % 100 != 11:
        return 'год'
    elif 1 < age % 10 <= 4 and age != 12 and age != 13 and age != 14:
        return 'года'
    else:
        return 'лет'
    
def pets_list():
    for key, value in pets.items():
        print(f"ID:{key}", value)
    
def create():
    last = collections.deque(pets, maxlen=1)[0]
    print("### Комманда create")
    key = input("Кличка питомца: ")
    fields = ["Вид", "Возраст", "Имя владельца"]
    tmp = {key: dict()}
    for field in fields:
        res = input(f"{field}: ")
        tmp[key][field] = int(res) if res.isnumeric() else res
        pets[last+1] = tmp

def read():
    print("### Комманда read")
    ID = int(input("Введите ID: "))
    pet = get_pet(ID)
    if not pet:
        print(f"Нет питомца с таким ID:{ID}")
        return
    key = [x for x in pet.keys()][0]
    string = f'Это {pet[key]["Вид"]} по кличке "{key}". ' \
        f'Возраст питомца: {pet[key]["Возраст"]} {get_suffix(pet[key]["Возраст"])}. ' \
            f'Имя владельца: {pet[key]["Имя владельца"]}'
    print(string)

def update(): #обновлять информацию об указанном питомце
    print("### Комманда update")
    ID = int(input("Введите ID: "))
    pet = get_pet(ID)
    if not pet:
        print(f"Нет питомца с таким ID:{ID}")
        return
    kkey = [x for x in pet.keys()][0]
    print("Введите данные или оставьте поле пустым. Нажмите Enter")
    tmp = dict()
    for key, value in pet[kkey].items():
        res = input(f"{key}: ")
        if res:
            tmp[key] = int(res) if res.isnumeric() else res
            pet[kkey].update(tmp)

def delete():
    print("### Комманда delete")
    ID = int(input("Введите ID: "))
    pets.pop(ID)

commands = {
"create": create,
"read": read,
"update": update,
"delete": delete,
"list": pets_list,
"stop": 0
}

def print_commands():
    print("Список доступных комманд:")
    for key in commands:
        print("> ", key)

while True:
    print_commands()
    command = input("Введите команду: ")
    if command not in commands.keys():
        continue
    if command == "stop":
        break
    commands[command]()
    input("Нажмите Enter чтобы продолжить")