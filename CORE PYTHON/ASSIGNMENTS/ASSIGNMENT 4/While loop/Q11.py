#11. WAP to check if given number Strong Number.

n = int(input("Enter the number:"))
org_n = n

sum = 0

while(n>0):
    d = n % 10
    n = n // 10
 


    i = 1
    fact = 1
    while(i<=d):
        fact *= i
        i+=1

    sum+=fact

if(org_n == sum):
    print(f"{org_n} is a strong number.")
else:
    print(f"{org_n} not a strong number.")
