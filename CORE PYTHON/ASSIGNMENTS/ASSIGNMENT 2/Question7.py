#7. Find the sum of three-digit number.

a = int(input("Enter the three-digit number:"))

#calculate the sum of three-digit numbers
a1 = a % 10
a = a // 10

a2 = a % 10
a3 = a // 10
sum = a1 + a2 + a3
print("Sum of thre-digit num:",sum)

