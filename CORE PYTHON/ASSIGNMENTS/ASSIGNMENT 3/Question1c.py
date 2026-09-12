#1.Write a program to check if the given number is positive or negative.

num = int(input("Enter the number:"))

if(num == 0):
    print("Given number is zero.")
elif(num < 0):
    print("Given number is negative.")
else:
    print("Given number is positive.")