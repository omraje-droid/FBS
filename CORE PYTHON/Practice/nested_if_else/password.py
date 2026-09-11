#7. Write a Python program to check whether a password contains exactly 8 characters and, if it does, check whether it contains at least one digit.

password = (input("Enter the password:"))

if len(password) == 8:
    print("Password is correct.")
    if any(ch.isdigit() for ch in password):
        print("correct Password.")
    else:
        print("Incorrect Password.")
else:
    print("Password must have exact 8 character or at last one digit.")