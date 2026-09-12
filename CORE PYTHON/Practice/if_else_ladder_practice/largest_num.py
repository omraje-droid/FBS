#6. Write a Python program to accept three numbers and find the largest number.
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
num3 = int(input("Enter the third number:"))

if(num1 > num2):
    if(num1 > num3):
        print("First number is grater than other two numbers.")
elif(num2 > num1):
    if(num2 > num3):
        print("Second number is grater than other two numbers.")
else:
    print("Third number is grater than other two numbers.")
    