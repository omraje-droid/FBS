#c. Find the sum of a geometric series from 1 to n where the common ratio is 2.

n  = int(input("Enter number:"))

i = 1
sum = 0
term = 1


while (i<=n):
    print(term ,end="")
    if (i<n):
        print(" +",end=" ")
    term *= 2
    sum += term
    i+=1

print("\nSum of a geometric series" ,sum)