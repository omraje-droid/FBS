#write a code to find simple interest .

p = int(input("Enter price:"))
r = int(input("Enter rate :"))
t = int(input("Enter time :"))

si = lambda p , r ,t : (p * r * t)/100

res = si (p,r,t)

print("Simple interst",res)