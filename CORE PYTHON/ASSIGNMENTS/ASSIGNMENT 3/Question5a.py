#5. Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.

a = int(input("Enter the first side:"))
b = int(input("Enter the second side:"))
c = int(input("Enter the third side:"))

if(a == b and b == c):
        print("Equilateral Triangle.")
elif(a == b or b == c or c == a):
        print("Isoscales Triangle.")
else:
    print("scalene Triangle.")