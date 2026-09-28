#9. WAP to print all numbers in a range divisible by a given number.
r =int(input("Enter the range:"))
n = int(input("Enter the number:"))
i = 1

while(i<r+1):
    if(i%n==0):
        print(i, end=" " )
    i+=1