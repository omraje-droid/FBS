#4. 4. Write a program to input all sides of a triangle and check whether triangle is valid or not.
 
a = int(input("Enter the first side:"))
b = int(input("Enter the second side:"))
c = int(input("Enter the third side:"))

if(a + b > c and a + c > b):
    if(c + b > a):
        print("Valid Triangle.")
    else:
        print("Invalid Triangle.")
else:
    print("The given sides cannot form a triangle.")
