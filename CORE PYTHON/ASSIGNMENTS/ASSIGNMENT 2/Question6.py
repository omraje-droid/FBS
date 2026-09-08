#6. WAP to calculate total salary of employee based on basic, da=10% of basic,ta=12% of basic, hra=15% of basic.
#DA = Dearness Allowance
#TA = Travel Allowance
#HRA = House Rent Allowance

basic_salary = float(input("Enter the Basic Salary :"))

# calculate the Dearness Allowance
DA = (10/100)*basic_salary

# calculate the Travel Allowance
TA = (12/100)*basic_salary

# calculate the House Rent Allowance'
HRA = (15/100)*basic_salary

Total_salary = DA + TA + HRA + basic_salary

print("Totel salary of employee :",Total_salary)