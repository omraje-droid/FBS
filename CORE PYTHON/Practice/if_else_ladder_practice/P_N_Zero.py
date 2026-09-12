#1. Write a Python program to accept a number and check whether it is positive, negative, or zero.
num = int(input("Enter the number:"))

if (num == 0):
    print("Given number is zero.")
elif (num >0):
     print("Given number is positive.")
else:
    print("Given  number is negative.")