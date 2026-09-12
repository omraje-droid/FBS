#2. Write a Python program to check whether a given number is positive and, if positive, check whether it is even or odd.

num = int(input("Enter the number:"))

if(num>0):
    print(num,"is positive.")
    if(num%2 == 0):
        print("Even number.")
    else:
        print("Odd number.")
else:
    print("Negative number.")