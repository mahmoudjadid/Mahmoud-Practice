

salary = float(input("please enter salary"))
month = input("please enter month name")
savings = float(input("please enter percentage of savings"))
electricity = float(input("please enter percentage of electricity"))
rent = float(input("please enter percentage of rent"))

s = (salary*savings)/100
e = (electricity*salary)/100
r = (rent*salary)/100
list =[e, s, r]
print (list)

def expences():
    totalEx=s + e + r
    totalAmount=salary - totalEx
    print (f"your total expences {totalAmount}")
    
def yearly():
    yearlye=e*12
    yearlyr=r*12
    totalyearexp=yearlye+yearlyr9    print (f"your total expences per year {totalyearexp}")
    
expences()
