# Program to Find the Roots of a Quadratic Equation ?
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))

#For the Quadratic equation we use  (ax sqrt 2)+bx+c

# for the Root of Quadratic equation will can perform like below
  
d = (b**2) - (4*a*c)

r1 = ((-b) + d ** 0.5)/(2*a)
r2 = ((-b) - d ** 0.5)/(2*a)

R = r1 + r2

print("Root of Given Quadratic equation is",R)


