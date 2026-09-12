#10.Write a Python program to accept a character and check whether it is an uppercase letter, lowercase letter, digit, or special character.

char = input("Enter only one character:")

if('A' <= char <= 'Z'):
    print("Given characteris upper class.")
elif('a' <= char <= 'z'):
    print("Given character is lowercase .")
elif('0'<=char <='9'):
    print("Given character is digit.")
else:
    print("Given character is special character.")