class Car:
    rang = None
    nom = None
    rusum = None
    tezlik = None
    status = False

    def start(self):
        self.status = True
        self.tezlik = 0
        return
    
    def t_kamaytirish(self, speed: int):
        if self.status is None:
            print('Moshinani start qil')
            return
        elif 0==self.tezlik or self.tezlik<speed:
            print('Moshinani tezligini kamaytirolmaysan')
            return
        self.tezlik = self.tezlik - speed
        print(f"Tezlik: {self.tezlik}")
        return
    
    def t_oshirish(self, speed: int):
        if self.status:
            self.tezlik = speed
            print(f"Tezlik: {self.tezlik}")
            return
        print('Moshinani start qil')
        return
    
    def signal(self):
        print('Signal chalindi')

    
car = Car()
car.rang = 'Qora'
car.rusum = 'Bugatti'
car.nom = 'Chiron'
car.start()
car.t_oshirish(50)
car.t_kamaytirish(10)

        


