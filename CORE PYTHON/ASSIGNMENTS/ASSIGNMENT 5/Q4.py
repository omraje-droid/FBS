#4. WAP to print Armstrong number within a given range
#(Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4)

num = int(input("Enter number :"))
org_num = num 
sum = 0
count = 0

while(num>0):
    count+=1

    num = num // 10



num = org_num 

for i in range(count):
    d = num % 10
    num = num // 10

    sum += d ** count

if(sum == org_num):
    print(f"{org_num} is an armstrong number.")
else:
    print(f"{org_num} is not an armstrong number.")
        

