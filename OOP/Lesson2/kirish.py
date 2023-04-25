# class Talaba():
#     def __init__(self, ism: str, familiya: str, yoshi: int):
#         self.ism = ism
#         self.fam = familiya
#         self.yosh = yoshi
#         self.guruh = None

#     def get_info(self):
#         return f"{self.ism}, {self.fam}, {self.yosh}, {self.guruh}"
    
#     def set_yosh(self, yosh: int):
#         self.yosh = yosh

#     def set_guruh(self, guruh: str):
#         self.guruh = guruh
    


    
# talaba1 = Talaba("Baxtiyor", "Ergashev", 25)
# talaba2 = Talaba('Bahodir', 'Jabborov', 20)



# # talaba1.yosh = 26
# talaba1.set_yosh(30)
# talaba1.set_guruh('218-17')
# talaba2.set_guruh('219-17')
# print(talaba1.get_info())
# print(talaba2.get_info())

from datetime import datetime, timedelta

class Parking():
    def __init__(self, name):
        self.name = name
        self.cars = []
        self.price = 8000

    def new_car(self, car):
        self.cars.append(car)

    def all_cars(self):
        for car in self.cars:
            print(car.get_info())

    def cars_count(self):
        return len(self.cars)
    
    def total_time(self, car):
        time = car.set_exit_time() + timedelta(minutes=30) - car.enter_time
        return time
    
    def total_price(self, car):
        time = self.total_time(car)
        return (time.total_seconds()/3600) * self.price

    
class Car():
    def __init__(self, number, model) -> None:
        self.number = number
        self.model = model
        self.enter_time = datetime.now()
        self.exit_time = None

    def get_info(self):
        return f"{self.number}, {self.model}"
    
    def set_exit_time(self):
        self.exit_time = datetime.now()
        return self.exit_time


p = Parking('Chorsu')

car1 = Car('01A777AA', 'BMW')
car2 = Car('01A001AA', 'Bugatti')
car3 = Car('01Z002ZZ', 'Ferrari')
car4 = Car('70A007KK', 'Onix')

# print(car2.get_info())

p.new_car(car1)
p.new_car(car2)
p.new_car(car3)
p.new_car(car4)
# print(p.cars_count())
# print(p.all_cars())
print(round(p.total_price(car3),2))