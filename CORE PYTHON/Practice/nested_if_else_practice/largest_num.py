#8. Write a Python program to accept three numbers, check whether the first number is greater than the second, and if it is, compare it with the third number to find the largest.
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
num3 = int(input("Enter the third number:"))

if(num1 >num2 ):
    if(num1 > num3):
        print("First number is greater then other numbers.")
    else:
        print("Third number is greater than other numbers.")
else:
    if(num2 > num3):
        print("Second number is greater then other number.")
    else:
        print("Third number is greater then other number.")