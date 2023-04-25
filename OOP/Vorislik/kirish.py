import datetime

class Bobo():
    def __init__(self, yosh: int, kasb: str) -> None:
        self.yosh = yosh
        self.kasb = kasb

    def get_info(self):
        return f"Yosh: {self.yosh} Kasb: {self.kasb} va {self.born_in()} yil tug'ilgan"
    
    def born_in(self):
        year = datetime.datetime.now().year - self.yosh
        return year
    

class Ota(Bobo):

    def __init__(self, yosh, kasb, ish_joyi):
        super().__init__(yosh, kasb, ish_joyi)
        self.ish_joyi = ish_joyi
        
    def get_job(self):
        return self.kasb
    
    def update_job(self, job):
        self.ish_joyi = job
        return self.ish
    
class Bola(Ota):
    pass

    
bobo = Bobo(55, 'Driver')

print(bobo.get_info())

ota = Ota(42, 'Programmer', 'Toshkent')
print(ota.get_job())

bola = Bola(15, 'Pupil', 'School')
print(bola.get_job())
