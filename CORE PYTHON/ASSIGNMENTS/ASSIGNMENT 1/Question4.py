# Write a program to enter P, T, R and calculate Simple Interest.

P = int(input("Principle Amount :"))
T = int(input("Time (in year) :"))
R = int(input("Rate of interest :"))

#P = Principle intrest
#T = Time in year like 1 , 2 , 3 years
#R = Rate of interets

# calculate simple interest (SI) 
SI = ( P * R * T)/100

print("Simple interest for above amount is",SI)