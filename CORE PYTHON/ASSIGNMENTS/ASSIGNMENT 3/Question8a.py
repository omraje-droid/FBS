#Write a program to prompt user to enter userid and password. 
# After verifying userid and password display a 4 digit random number and ask user to enter the same.
# If user enters the same number then show him success message otherwise failed. (Something like captcha)
import random

correct_userid = "Omraje@123"
correct_password = "98765432"

userid = input("Enter the userid:")
password = input("Enter the password:")

if userid == correct_userid and password == correct_password  :
    print("Given userid and password verifying.")

    captcha = random.randint(1000 , 9999)

    print("Enter the Captcha:",captcha)

    user_captcha = int(input("Enter the captcha:"))

    if(user_captcha == captcha ):
        print("Succesful to login.")
    else:
        print("Incorrect Captcha.")
else:
    print("Incorrect password and userid.")
