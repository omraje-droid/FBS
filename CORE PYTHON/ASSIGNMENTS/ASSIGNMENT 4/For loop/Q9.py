#9. WAP to print all numbers in a range divisible by a given number.

n = int(input("Enter the range:"))
a = int(input("Enter the divisible number:"))
for i in range(1,n+1):
    if(i%a == 0):
        print(i,end =" ")