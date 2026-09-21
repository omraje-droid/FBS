#10. Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)

male_age = int(input("Enter the male age :"))
female_age = int(input("Enter the female age :"))

if (male_age >= 21 and female_age >= 18):
    print("Eligible for marry.")
else:
    print("Not Eligible for marry.")