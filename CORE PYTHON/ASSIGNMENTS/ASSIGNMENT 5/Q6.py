#6. Write a program to print first n prime numbers.

n = int(input("Enter number:"))

count = 0
num = 2

while count < n:
    i = 1
    c = 0

    while i <= num:

        if num % i == 0:
            c += 1

        i += 1

    if c == 2:
        print(num)
        count += 1
    
    num += 1
