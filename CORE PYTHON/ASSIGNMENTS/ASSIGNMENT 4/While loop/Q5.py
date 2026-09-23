#5. WAP to print Fibonacci series upto n.
n = int(input("Enter number:"))

a = -1
b = 1
i = 1

while(i<n+1):
    c = a + b
    print(c)
    a = b
    b = c
    i += 1