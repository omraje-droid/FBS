#4. Write a Python program to check whether the entered username is correct and, if correct, check whether the entered password is correct.
name = (input("Enter the username:"))
password = (input("Enter the password:"))

if len(name) == 10:
    print("Username is correct:",name)

    if len (password) == 8:
        print("Password is correct:",password)
    else:
        print("Password is incorrect:",password)

else:
    print("Username is incorrect:",name)