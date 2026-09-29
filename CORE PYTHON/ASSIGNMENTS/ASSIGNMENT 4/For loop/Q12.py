#12. Write a program to check if given number is Armstrong number or not.
#(Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4)


n = int(input("Enter the number:"))
org_num = n
sum = 0
count = 0

while(n>0):
    count+=1
    n = n // 10


n = org_num
for i in range(count):
    d = n % 10
    n = n // 10    
    sum = sum + d ** count

if(sum == org_num ):
    print(f"{org_num} is an armstrong number.")
else:
    print(f"{org_num} is not an armstrong number.") 