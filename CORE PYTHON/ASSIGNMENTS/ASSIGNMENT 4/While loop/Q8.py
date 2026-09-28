#8. WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.
n = int(input("Enter the range:"))

i=1

while(i<n+1):
    a = i * 5
    if(a%7 == 0):
        print(a)
    i+=1
