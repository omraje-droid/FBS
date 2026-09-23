#3. WAP to print sum of series upto n.
n =int(input("Enter number:"))

sum = 0
i = 1

while(i<=n):
    sum += i
    print(sum,end =" ")
    i+=1