#1. Write a program to prompt user to enter userid and password. If Id and password is incorrect give him chance to re-enter the credentials. 
# Let him try 3 times. After that program to terminate.
id = "omraje123"
key = "om1234"

for i in range(3):
    userid = input("Enter the userid:")
    password = input("Enter the password:")
    if(userid == id and password == key):
        print("Userid and Password is correct.")
        break
    
    else:
        print("Incorrect try again .")
    