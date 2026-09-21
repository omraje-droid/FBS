#12. Write a program to check if given 3 digit number is a palindrome or not.

num = int(input("Enter the three digit number:"))
number = num
d = num % 10
num = num // 10

d2 = num % 10
num = num // 10

d3 = num % 10
num = num // 10

reverse = d*100 + d2*10 + d3

if (reverse == number):
    print("Palindrome.")
else:
    print("Not Palindrome.")