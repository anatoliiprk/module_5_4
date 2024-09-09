print()
print('Задача "История строительства"')
print('----------')
print()

class House:
    houses_history = []

    def __new__(cls, *args):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name: str, number_of_floors: int):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor: int):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)
        print()

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors <= other

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors > other

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors >= other

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors != other

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        elif isinstance(value, House):
            self.number_of_floors += value.number_of_floors
            return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

    def __sub__(self, other):
        if isinstance(other, int):
            if other >= self.number_of_floors:
                return 'Такого кол-ва этажей не существует'
            else:
                self.number_of_floors -= other
                return self
        elif isinstance(other, House):
            if other.number_of_floors >= self.number_of_floors:
                return 'Такого кол-ва этажей не существует'
            else:
                self.number_of_floors -= other.number_of_floors
                return self

    def __mul__(self, other):
        if isinstance(other, int):
            self.number_of_floors *= other
            return self
        elif isinstance(other, House):
            self.number_of_floors *= other.number_of_floors
            return self

    def __truediv__(self, other):
        if isinstance(other, int):
            self.number_of_floors = self.number_of_floors // other
            return self
        elif isinstance(other, House):
            self.number_of_floors = self.number_of_floors // other.number_of_floors
            return self

    def __floordiv__(self, other):
        if isinstance(other, float):
            if self.number_of_floors % other != 0:
                return 'Такого кол-ва этажей не существует'
            else:
                self.number_of_floors = self.number_of_floors / other
                return self
        elif isinstance(other, House):
            self.number_of_floors = self.number_of_floors / other.number_of_floors
            return self

    def __del__(self):
        print(f'{self.name} снесён, но остается в истории')

h1 = House('ЖК Горский', 10)
print(House.houses_history)
h2 = House('ЖК Эльбрус', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)