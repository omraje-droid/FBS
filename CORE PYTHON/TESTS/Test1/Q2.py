#2. write a program to calculate simple interest based on principle , Rate and Time (SI = P*R*T/100)

p = int(input("Enter the principle value:"))
r = int(input("Enter the rate value:"))
t = int(input("Enter the time:"))

SI = (p * r * t)/100

print("Simple Interest:",SI)