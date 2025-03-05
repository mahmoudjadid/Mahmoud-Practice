
salary = float(input("please enter salary"))
month = input("please enter month name")
savings = float(input("please enter percentage of savings"))
electricity = float(input("please enter percentage of electricity"))
rent = float(input("please enter percentage of rent"))
xtrasavings=float(input("please enter the extra amount saved, if none enter 0"))
salaryup = bool("is there a raise in salary ?")

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
    totalyearexp=yearlye+yearlyr9    
    print (f"your total expences per year {totalyearexp}")

def xtsavper():
    xtsavper= (xtrasavings/savings)/100
    print (f"your extra saving percentage is {xtsavper}")
    
def raiseinsalary():
    
    if salaryup==True:
        newsalary=salary**2    
        print("the new salary is", {newsalary})
        
expences()
raiseinsalary()