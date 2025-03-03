
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
        carname=input("enter car name: ")
        days=int(input("enter the number of days: "))
        if (carname=="BMW"):
            totalrent=veh1.rentpr*days
        elif (carname=="KIA"):
            rentprice=veh2.rentpr*days
        elif (carname=="toyota"):
            rentprice=veh3.rentpr*days    
        print(self.rentpr * days)
            
veh1=car("BMW", 2020, 40, 4 ,120)
veh2=car("KIA", 2022, 30, 5, 90)
veh3=car("toyota", 2019, 35, 7, 130)

veh1.totalrent()
