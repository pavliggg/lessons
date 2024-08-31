class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        self.apartments = []
        self.residents = []

    def add_apartment(self, apartment):
        self.apartments.append(apartment)

    def add_resident(self, resident):
        self.residents.append(resident)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)
print(len(h1))
print(len(h2))