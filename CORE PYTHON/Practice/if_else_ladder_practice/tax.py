#9.Write a Python program to accept a person's salary and calculate the tax according to different salary ranges
salary = int(input("Enter the salary:"))

if(salary <= 250000):
    print("GIven salary will not having tax.")
elif(salary <= 400000):
    tax = (salary * 5) / 100
    print(f"Given salary having tak : {tax}.")
elif(salary <= 700000):
    tax = (salary * 20) / 100
    print(f"Given salary having tax : {tax}.")
else:
        tax = (salary * 30) /100
        print(f"Given salary having tax : {tax}.")