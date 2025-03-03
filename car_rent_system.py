
class motors:
    def __init__(self, name, year, rentprice, engcapa):
        self.year=year
        self.rentpr=rentprice
        self.engcap=engcapa
        self.name=name 
        
class car(motors):
    
    def __init__(self, name, year, rentprice, engcapa, seats):
        
        self.seats=seats    
        super() .__init__(name, year, rentprice, engcapa)

    def totalrent(self):
        name=None
        carname=input("enter car name: ")
        days=int(input("enter the number of days: "))
        if self.name=="name":
         totalrent=self.rentpr*days 
         print(totalrent)
            
veh1=car("BMW", 2020, 40, 4 ,120)
veh2=car("KIA", 2022, 30, 5, 90)
veh3=car("toyota", 2019, 35, 7, 130)

veh1.totalrent()
