#5. Write a Python program to accept a month number and display the number of days in that month.
num = int(input("Enter the month number:"))

if(num > 12):
    print("Invalid number.")
elif(num < 1):
    print("Invalid number.")
elif(num == 1):
    print("January")
elif(num == 2):
    print("February")
elif(num == 3):
    print("April")
elif(num == 4):
    print("March")
elif(num == 5):
    print("May")
elif(num == 6):
    print("June")
elif(num == 7):
    print("July")
elif(num == 8):
    print("August")
elif(num == 9):
    print("September")
elif(num == 10):
    print("Octember")
elif(num == 11):
    print("November")
else:
    print("December")
    