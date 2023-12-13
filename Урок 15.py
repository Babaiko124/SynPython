# Задание 1
class Transport:
   def __init__(self, name, max_speed, mileage):
       self.name = name
       self.max_speed = max_speed
       self.mileage = mileage

bus = Transport('ПАЗ', 60, 100000)
print(f'Название автобуса: {bus.name}. Скорость: {bus.max_speed}. Пробег: {bus.mileage}')

# Задание 2
class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    
    def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name} {capacity} пассажиров"

class Autobus(Transport):
    def seating_capacity(self, capacity = 50):
        return super ().seating_capacity (capacity = 50)

bus = Autobus("Лиаз", 180, 12)
print(bus.seating_capacity())