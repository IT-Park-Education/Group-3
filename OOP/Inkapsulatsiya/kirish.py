class Avto():
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price
        self.__km = 0
    
    def update_km(self, km):
        self.__km = km

    def is_equal(self, other):
        return self.price == other.price

    def __eq__(self, other):
        return self.price == other.price

    def __add__(self, other):
        return self.price + other.price

    def __pow__(self, number):
        return self.price ** number

    def is_not_equal(self, other):
        return self.price != other.price
    
    def __or__(self, other):
        return self.price >15000 or other.price<15000

    def __gt__(self, other):
        return self.price > other.price

    def __str__(self) -> str:
        return self.name + ": " + str(self.price) + " | " + str(self.__km) + " km"
    
class AvtoSalon():
    def __init__(self, name):
        self.name = name
        self.cars = []

    def add_cars(self, *args):
        self.cars += list(args)

    def get_cars(self):
        for car in self.cars:
            print(car)

    def __str__(self) -> str:
        return self.name + ' | ' + str(len(self.cars))
    
a1 = Avto('Malibu', 3)
a2 = Avto('Damas', 8000)
a3 = Avto('Nexia3', 11000)
a2.update_km(40)
# a2.__km = 50

s = AvtoSalon('GM')
# s.add_cars(a1,a2,a3)
# s.get_cars()
# print(s)
# print(a2)
# print(a1.is_equal(a3))
# print(a2.is_not_equal(a3))
# print(a1.is_big(a3)) # a1 > a3
print(a1 > a3)
print(a2 == a3)
print(a2 + a3)
print(a1.price ** 3)
print(a1 | a2)
# print(dir(a1))