#1. Write a Python program to check whether a person is eligible to vote and, if eligible, check whether the person is a senior citizen.
age = int(input("Enter the age:"))

if(age>18):
    print("Eligible for vote.")
    if(age > 50):
        print("Senior citizen.")
    else:
        print("younger guy.")
else:
    print("Not eligiible for vote.")