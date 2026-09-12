#8. Write a Python program to accept an electricity consumption unit and calculate the electricity bill according to different unit ranges.

unit = float(input("Enter electricity unit:"))

if (unit <= 100):
    bill = unit * 5
    print("Electricity Bill is",bill)
elif(unit <= 200):
    bill = unit * 7
    print("Eletricity Bill is",bill)
elif(unit <= 300):
    bill = unit * 10
    print("Electricty Bill is",bill)
else:
        bill = unit * 15
        print("Electricity Bill is",bill)