# class Avto():
#     def __init__(self, name, price) -> None:
#         self.name = name
#         self.price = price
#         self.km = 0

#     def info(self):
#         return self.name + ": " + str(self.price) + " | " + str(self.km) + " km"
    
#     def update_km(self, km):
#         self.km = km
    
# class AvtoSalon():
#     def __init__(self, name):
#         self.name = name
#         self.cars = []

#     def add_cars(self, *args):
#         self.cars += list(args)

#     def get_cars(self):
#         for car in self.cars:
#             print(car.info())
    
# a1 = Avto('Malibu', 35000)
# a2 = Avto('Damas', 8000)
# a3 = Avto('Nexia3', 11000)
# a2.update_km(40)

# s = AvtoSalon('GM')
# s.add_cars(a1,a2,a3)
# s.get_cars()


#1
# class Talaba:
#     def __init__(self, name:str, age:int):
#         self.name=name
#         self.age=age
#         self.fanlar = []

#     def get_info(self):
#         return f"ismi: {self.name}" \
#                f"\nyoshi: {self.age}"

#     def add_fan(self, *args):
#         self.fanlar += list(args)

#     def spiska_fan(self):
#         print(f"\n{self.name}ning fanlar ro'yxati: ")
#         for fan in self.fanlar:
#             print(f"{fan.get_fan()}")


#     def remove_fan(self,fan):
#         if fan in self.fanlar:
#             self.fanlar.remove(fan)
#             print("Removed fan")
#         else:
#             return f"Siz bu {fan}ga yozilmagansiz!"

# class Fan:
#     def __init__(self,nomi):
#         self.nom=nomi

#     def get_fan(self):
#         return self.nom


# talaba=Talaba("Bahodir",21)

# mat=Fan("oliy matematika")
# fiz=Fan("Elektronika")
# eng=Fan("English")
# pro=Fan("Python")
# phy=Fan("Jismoniy tarbiya")

# talaba.add_fan(mat,eng,pro, phy)
# talaba.spiska_fan()
# print('===================================')
# talaba.remove_fan(mat)
# talaba.spiska_fan()


#3
# class Avtosalon():
#     def __init__(self, nomi, manzili):
#         self.nomi=nomi
#         self.manzil=manzili
#         self.sotuvdagi=['spark', 'lacetti', 'nexia3', 'cobalt']
#         self.avtomobillar=[]

#     def add(self,*cars):
#         self.avtomobillar += list(cars)

#     def get_cars(self):
#         for i,car in enumerate(self.avtomobillar):
#             print(f"{i+1}-mashina:\n{car.get_info()}")
#         print()

#     def remove(self,car): #4
#         if car in self.avtomobillar:
#             self.avtomobillar.remove(car)
#             print(f"# # # # # # # # # # # # # # # #\n "
#                   f"{car.nom} ro'yxatdan o'chirildi..."
#                   f"\n# # # # # # # # # # # # # # # #\n")



# class Mashina():
#     def __init__(self,nomi,yili,rangi):
#         self.nom=nomi
#         self.yil=yili
#         self.rang=rangi
#         self.km=0

#     def get_info(self):
#         return f"nomi: {self.nom} " \
#                f"\nyili: {self.yil} " \
#                f"\nrangi: {self.rang} " \
#                f"\nkm: {self.km}"

#     def update_km(self,km:int):
#         self.km = km

# car1=Mashina("BMW",2022,"qora")
# car2=Mashina("LAMBORGINI",2023,"sariq")
# car3=Mashina("Porsche",2021,"qizil")

# a1=Avtosalon("Avtosalon","M.Ulug'bek")

# a1.add(car1,car2,car3)
# a1.get_cars()
# a1.remove(car1)
# a1.get_cars()

# #5
# car2.update_km(57)
# print(car2.get_info())


#6
class SHAXS():
    def __init__(self,ism:str,fam:str,t_yil:int,jins:str,tel:str):
        self.ism=ism
        self.familiya=fam
        self.tyil=t_yil
        self.jins=jins
        self.tel=tel


    def get_ism(self):
        return self.ism

    def get_fam(self):
        return self.familiya

    def get_tyil(self):
        return self.tyil

    def get_jins(self):
        return self.jins

    def get_tel(self):
        return self.tel


talabalar = {}

class TALABA(SHAXS):
    def __init__(self,ism:str,fam:str,t_yil:int,jins:str,tel:str,guruh:str,kurs:int):
        super().__init__(ism,fam,t_yil,jins,tel)
        self.guruh=guruh
        self.kurs=kurs

    def get_info(self):
        print(f"ism:{self.ism}"
              f"\nfamiliya: {self.familiya}"
              f"\ntyil: {self.tyil}"
              f"\njins: {self.jins}"
              f"\ntel: {self.tel}"
              f"\nguruh: {self.guruh}"
              f"\nkurs: {self.kurs}\n")
        
def search_phone(phone, ism=None):
    if ism is not None:
        talaba = talabalar.get(ism)
        if talaba is None:
            print('Talaba topilmadi')
        else:
            print('#############')
            talaba.get_info()
        return

    for obj in talabalar.values():
        if phone in obj.get_tel():
            obj.get_info()

t1=TALABA("Bahodir","Abdusaxatov",2002,"Erkak","+998907177749","314-19",4)
t2=TALABA("Bekzod","Rizayev",2000,"Erkak","+998904207747","112-20",3)
t3=TALABA("Baxtiyor","Mirzayev",2316,"Erkak","+998901321921","112-20",3)
talabalar.update({t1.get_ism():t1})
talabalar.update({t2.get_ism():t2})
talabalar.update({t3.get_ism():t3})
# t1.get_info()
# t2.get_info()
# print(talabalar)

search_phone('777')