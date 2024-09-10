class Animal:
    alive = True   # Живое
    fed = False    # Накормленное

    def __init__(self, name):
        self.name = name   # Имя животного

    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

# Определяем класс Mammal, наследующий от Animal
class Mammal(Animal):
    pass

# Определяем класс Predator, наследующий от Animal
class Predator(Animal):
    pass

# Определяем родительский класс Plant
class Plant:
    edible = False  # Съедобность

    def __init__(self, name):
        self.name = name  # Имя растения

# Определяем класс Flower, наследующий от Plant
class Flower(Plant):
    pass

# Определяем класс Fruit, наследующий от Plant
class Fruit(Plant):
    edible = True  # Фрукты съедобные

# Создаем объекты классов
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

# Выводим информацию об объектах
print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)

# Применяем метод eat
a1.eat(p1)  # Хищник пытается съесть цветок
a2.eat(p2)  # Млекопитающее ест фрукт

# Выводим состояние после действий
print(a1.alive)
print(a2.fed)
