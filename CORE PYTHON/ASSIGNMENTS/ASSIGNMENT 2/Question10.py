#10. Write a program to reverse three-digit number.
num = int(input("Enter the three-digit numbers:"))

# calculate the reverse three-digit number
a = num 
a1 = a % 10
a = a // 10 
a2 = a % 10 
a3 = a // 10 
print(f"Reverse of three-digit number {num} is {a1}{a2}{a3}")