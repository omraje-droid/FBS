#5. WAP to print Fibonacci series upto n.
n = int(input("Ente number:"))

a =-1
b = 1

for i in range(1,n+1):
    c=a+b
    print(c)
    a=b
    b=c
    i+=1