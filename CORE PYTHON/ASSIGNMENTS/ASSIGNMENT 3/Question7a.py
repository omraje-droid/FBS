#7. Write a program to check if user has entered correct userid and password.

userid = input("Enetr the User id :")
password = input("Enter the password:")

if len(password) == 8:
    if len(userid) == 10:
        print("Correct userid and password.")
    else:
        print("Incorrect Userid.")
else:
    print("Incorrect Password")
    