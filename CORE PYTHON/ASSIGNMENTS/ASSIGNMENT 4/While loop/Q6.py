#6. WAP to check if a given number is prime number or not.

n = int(input("Enter the number:"))
count = 0
i=2

while(i<n):
    if(n%i == 0):
        count = count+i
    i+=1

if count == 0:
    print("Prime")
else:
    print("Not Prime.")

   
