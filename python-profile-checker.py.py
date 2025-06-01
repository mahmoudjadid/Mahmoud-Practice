

name=str(input("enter your name: "))
age=int(input("enter your age:"))
gpa=float(input("enter your GPA: "))
foi=input("enter your feild of interest: ")
grad=bool(input("are you graduated ?"))


if age > 25 and gpa >=3.5 and grad==True:
    print("you are eligible for scholarship")
elif age > 30 and gpa >= 2.5 :
    print("your are eligible for internship")
else:
    print("we recommend you to apply later")




#   >  <