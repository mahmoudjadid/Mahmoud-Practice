class veh:
  def __init__(self, name, year, rent, seats):
    self.name = name
    self.age = year
    self.rent = rent
    self.seats = seats

p1 = veh("BMW", 2020, 55, 6)

print(p1.name, p1.age, p1.rent, p1.seats)
