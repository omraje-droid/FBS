#5 .Write a Python program to check whether a person is eligible for a driving license and, if eligible, check whether the person is above 60 years old.

age = int(input("Enter the age:"))

if(age >= 18 ):
    print("Eligible for a driving license.")
    if(age > 60 ):
        print("Eligible for driving license and age is above 60.")
    else:
        print("Eligible for driving licence but age is below 60.")
else:
    print("Not eligible or a driving license.")