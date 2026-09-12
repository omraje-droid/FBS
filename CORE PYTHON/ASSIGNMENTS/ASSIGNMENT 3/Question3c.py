#3. Write a program to input angles of a triangle and check whether triangle is valid or not.
angle1 = int(input("Enter the first angle:"))
angle2 = int(input("Enter the second angle:"))
angle3 = int(input("Enter the third angle:"))

sum = angle1 + angle2 + angle3

if(sum < 180):
    print("Given angles sum is less than 180.the triangle is invalid")
elif(sum > 180):
    print("Given angles sum is grater than 180, the triangle is invalid.")
else:
    print("Given angles sum is 180, so the triangle is valid.")