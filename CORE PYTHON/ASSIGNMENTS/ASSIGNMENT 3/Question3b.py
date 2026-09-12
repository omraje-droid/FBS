#3.Write a program to input angles of a triangle and check whether triangle is valid or not.
angle1 = int(input("Enter the first angle:"))
angle2 = int(input("Enter the second angle:"))
angle3 = int(input("Enter the third angle:"))

sum = angle1 + angle2 + angle3

if(sum <= 180):
    if(sum == 180):
        print("The given angles form valid triangle.")
    else:
        print("The given angles do not form valid triangle.")
else:
    print("The given angle sum is grater than 180 ")