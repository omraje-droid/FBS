#4. WAP to print factorial of a number .

n = int(input("Enter number:"))

fact = 1
i = 1

while(i<=n):
    fact *= i
    print(fact,end=' ')
    i+=1