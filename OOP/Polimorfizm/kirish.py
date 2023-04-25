class Shaxs:
    def __init__(self, ismi, yoshi) -> None:
        self.name = ismi
        self.age = yoshi

    def info(self):
        print(self.name, self.age)
    
class Professor(Shaxs):
    
    def info(self):
        print(f"Ismi: {self.name}, Yoshi: {self.age}")
        
class Foydalanuvchi(Shaxs):
    
    def info(self):
        print(f"Ism: {self.name} Yosh: {self.age}")

p1 = Professor('Baxtiyor', 25)
p1.info()
f1 = Foydalanuvchi('Bahodir', 20)
f1.info()