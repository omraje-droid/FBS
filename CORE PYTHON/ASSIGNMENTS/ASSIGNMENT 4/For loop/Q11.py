#11. WAP to check if given number Strong Number.

n = int(input("Enter the number:"))
org_n = n
sum=0

while(n>0):
    d=n%10
    n=n//10

    fact = 1
    for i in range(1,d+1):
        fact*=i

    sum+=fact
if(sum == org_n):
    print(f"{org_n} is a strong number.")
else:
    print(f"{org_n} is not a strong number.")



#strong number means (145)= 1*1 + 4*3*2*1 + 5*4*3*2*1 = 1+24+120 = 145 after the end we get the oringinal number is called strong number. 