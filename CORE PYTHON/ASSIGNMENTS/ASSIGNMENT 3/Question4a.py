#4. 4. Write a program to input all sides of a triangle and check whether triangle is valid or not.

a = int(input("Enter the first length:"))
b = int(input("Enter the second length:"))
c = int(input("Enter the third length:"))

if(a+b > c and b+c > a and a+c > b):
    print("Vaild Triangle.")
else:
    print("Invalid Triangle.")
    
    