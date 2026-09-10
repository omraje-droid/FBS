# 10. Write a Python program to check whether the entered password is correct or incorrect.
p = str(input("Enter the password:"))

if len(p) == 8:
    print("Password is correct.")
else:
    print("Password is incorrect.")