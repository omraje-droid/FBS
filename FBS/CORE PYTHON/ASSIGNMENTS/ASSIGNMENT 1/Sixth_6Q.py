#Write a Program to input two angles from user and find third angle of the triangle ?

a = int(input("Enter the first angle:"))
b = int(input("Enter the second angle:"))

# a & b give the two angle we can find third angle

c = 180-b-a 

print("Third angle is",c)