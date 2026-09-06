# Q. Program to find quotient and reminder of two numbers
Divisor = int (input("Enter the divisor value :")) 
Dividend = int(input("Enter the dividend value :"))

# Result of  Dividend / Divisor 
Result = Dividend / Divisor

# Calculate Quotient
Quotient = Dividend // Divisor

# Calculate Reminder
Reminder = Dividend % Divisor

print("Division of", Divisor , "&", Dividend , "is",Result)
print("Quotient of", Divisor,"&",Dividend,"is",Quotient)
print("Reminder of",Divisor,"&",Dividend,"is",Reminder)