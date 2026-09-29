#12. Write a program to check if given number is Armstrong number or not.
#(Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4)

num = int(input("Enter a number:"))
org_num = num
sum = 0
count = len(str(num))
for i in range(count):
    d = num % 10
    num = num // 10

    sum = sum + d ** count

if(sum == org_num):
    print(f"{ org_num} is an amnstrong number.")
else:
    print(f"{org_num} is not an amnstrong number.")