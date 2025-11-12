salary=int(input("salary:"))
age=int(input("age:"))
if(salary>=20000 and age<=25):
    loan=int(input("loan"))
    if(loan>50000):
        print("max loan is 50000")
    else:
     print("Eligible for loan")
else:
    print("Not Eligible for loan")