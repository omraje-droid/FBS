num = int(input("Enter the number:"))
sum = 0
while(num > 0):
    d = num % 10
    num = num // 10 
    sum = sum + d
    print(sum)