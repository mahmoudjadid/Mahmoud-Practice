

class vehicle:
    
    name= None
    year=0
    seats=0
    rentprice=0.0
    engcapa=0.0
    
    def __init__(self, name, year, seats, rentprice, engcapa):
        self.name = name
        self.year=year
        self.seats=seats
        self.rentprice=rentprice
        self.engcapa=engcapa
    
    
veh1=vehicle("BMW", 2020, 4, 40 ,120)
veh2=vehicle("KIA", 2022, 5, 30, 90)
veh3=vehicle("toyota", 2019, 7, 35, 130)


def days():
    input=("enter the number of days: ")

def totalrent():
    totalrent=vehicle.rentprice*days    
    return totalrent

print(veh1.name)
 
    