
class motors:
    
    name= None
    year = 0
    rentprice = 0.0
    engcap = 0.0 
    
    def __init__(self, name, year, rentprice, engcapa):
        self.year=year
        self.rentprice=rentprice
        self.engcap=engcapa
        self.name=name 
        
class car(motors):
    
    def __init__(self, name, year, rentprice, engcapa, seats):
        
        self.seats=seats    
        super() .__init__(name, year, rentprice, engcapa)

    def totalrent(self, name , year, ):
        self.totalrent=0
        name=None
        carname=input("enter car name: ")
        days=int(input("enter the number of days: "))
        if self.name=="name":
         totalrent=self.rentpr*days 
         print(totalrent)
         return self.totelrent
    totalrent()
    
            
veh1=car("BMW", 2020, 40, 4 ,120)
veh2=car("KIA", 2022, 30, 5, 90)
veh3=car("toyota", 2019, 35, 7, 130)

print(veh1.name, veh1.year, veh1.engcap, veh1.seats, veh1.rentpr)
print(veh2.name, veh2.year, veh2.engcap, veh2.seats, veh2.rentpr)
print(veh3.name, veh3.year, veh3.engcap, veh3.seats, veh3.rentpr)


