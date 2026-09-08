#11. Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.
integer_amount = int(input("Enter the integer amount :"))

# calculate the minimum numbers of notes
amount = integer_amount

a = amount // 500
amount = amount % 500
b = amount // 200 
amount = amount % 200
c = amount // 100
amount = amount % 100
d = amount // 50
amount = amount % 50
e = amount // 20
amount = amount % 20
f = amount // 10
remaninig = amount % 10

sum = a+b+c+d+e+f

print(f"The minimum number of notes for amount {integer_amount} is {sum} notes. ")
print(f"Remaning amount without notes is {remaninig}.")
