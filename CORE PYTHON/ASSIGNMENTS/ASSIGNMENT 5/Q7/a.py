#a. 1! + 2! + 3! + 4! + .....n!

a = int(input('Enter number:'))

i = 1
sum = 0
fact = 1
while(i <= a):
    fact*=i
    sum += fact
    print(f"{i}! ",end="")
    if i < a:
        print("+", end =" ")
    i+=1

print(f"\nSum of all {sum}")
    
   

   