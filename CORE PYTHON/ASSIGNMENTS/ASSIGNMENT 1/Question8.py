#Write a program to convert days into years, weeks and days.

days = int(input("Enter Days:"))

year = days // 365
days = days % 365
print ("Years :",year)

weeks = days // 7

print ("Weeks :",weeks)

days = days % 7 
print ("Remaining days ",days)
