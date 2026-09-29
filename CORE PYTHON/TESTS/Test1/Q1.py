#write a program to find the area and perimeter of following figure(Accept the length , breadth and radius from user )

length = int(input("Enter the length:"))
breadth = int (input("Enter the breadth:"))
radius = int(input("Enter the radius:"))
pie = 3.14


rectangle_area = length * breadth

semicircle_area = (pie * (radius**2)) / 2

area = rectangle_area + semicircle_area

perimeter = 2*length + breadth + pie * radius

print("Area of given firgure:",area)

print("Perimeter of given figure:",perimeter)
