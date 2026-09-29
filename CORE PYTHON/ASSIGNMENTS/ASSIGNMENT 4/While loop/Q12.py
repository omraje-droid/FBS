#12. Write a program to check if given number is Armstrong number or not.
#(Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4)

n = int(input("Enter the number:"))
sum = 0

while(n>0):
    d = n % 10
    n = n // 10

    sum = sum + d ** 3

    print(sum)
