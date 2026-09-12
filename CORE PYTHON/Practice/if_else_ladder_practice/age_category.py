#3. Write a Python program to accept a person's age and display whether the person is a child, teenager, adult, or senior citizen.

age = int(input("Enter the age:"))

if(age < 10):
    print(f"Given age is children.")
elif(age < 18):
    print("Given age is teenage.")
elif(age < 40):
    print("Given age is adult.")
elif(age >= 55):
    print("Given age is senior citizen.")