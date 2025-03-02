class vehicle:
    
    def __init__(self, name, year, rentprice, engcapa, seats):
        self.name = name
        self.year=year
        self.seats=seats    
        self.rentprice=rentprice
        self.engcapa=engcapa
    
    def totalrent(self):
        carname=input("enter car name: ")
        days=int(input("enter the number of days: "))
        if (carname=="BMW"):
            totalrent=veh1.rentprice*days
        elif (carname=="KIA"):
            rentprice=veh2.rentprice
        print(self.rentprice * days)
            
veh1=vehicle("BMW", 2020, 40, 4 ,120)
veh2=vehicle("KIA", 2022, 30, 5, 90)
veh3=vehicle("toyota", 2019, 35, 7, 130)
      
veh1.totalrent()