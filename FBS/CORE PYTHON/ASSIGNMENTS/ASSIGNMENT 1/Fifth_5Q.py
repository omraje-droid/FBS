#Write a program to enter P, T, R and calculate Compound Interest.
P = int(input("Enter the principle amount :"))
T = int(input("Enter the Time in Year format :"))
R = int(input("Enter the Rate of Interest "))

#Calculate Compound Interest
A = (1+(R/100))**T
CI = (P*A)-P
print("Compound Interest is :",CI)
