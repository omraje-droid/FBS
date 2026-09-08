#9. Write a program to swap two numbers without using third variable.
a = int(input("Enter the first num:"))
b = int(input("Enter the second num:"))

# swapping first and second without third variable.
a = a + b 
b = a - b 
a = a - b

print("First num swapped without using third variable:",a)
print("Second num swapped without using third variable:",b)