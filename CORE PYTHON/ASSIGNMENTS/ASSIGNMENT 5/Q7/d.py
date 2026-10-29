#d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10


n = int(input("Enter num:"))
sum = 0 

for i in range(1,n+1):
    if(i<=1):
        print(i,end="")
    else:
        print(f"a{i}/{i}",end="")

        b = n ** i / i

        sum += b
    if (i<n):
        print("+",end=" ")

print(f"\nsum of series:{sum}")