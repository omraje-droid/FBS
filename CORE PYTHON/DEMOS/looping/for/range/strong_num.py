num = int(input("Enter the number:"))
org_num = num
sum = 0

while(num > 0 ):
    d = num % 10
    #print(d)
    num = num // 10

    fact = 1
    for i in range(1 ,d+1):
        fact *= i
       # print(fact)

    sum += fact
if(sum == org_num):
     print(f"{org_num} is a strong number.")
else:
     print(f"{org_num} is not a strong number.")