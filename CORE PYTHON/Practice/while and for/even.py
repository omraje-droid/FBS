# WAP to print all even numbers until n.

n = int(input(" Enter the range:"))
i = 1
while (i<=n):
    if (i%2==0):
        print(i)
    i+=1
     

#12345678910


n = int(input("Enter a range:"))
for i in range(1,n+1):
    if(i%2 != 0):
        print (i)
