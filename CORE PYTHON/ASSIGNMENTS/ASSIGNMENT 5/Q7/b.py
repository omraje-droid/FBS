#b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)
n = int(input("Enter Range:"))

i = 1

while (i <= n ):
    if (i>1):
        print(f"N ^ {i} ",end="")
    else:
        print("N ",end="")
    if(i < n):
        print("+" ,end=' ')        

    i+=1

