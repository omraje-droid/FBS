#4. Write a Python program to accept a number from 1 to 7 and display the corresponding day of the week.
num = int(input("Enter the number of Day:"))

if(num > 7):
    print("Given number is invalid.")
elif(num < 1):
    print("Given number is invalid.")
elif(num == 1):
    print("Monday.")
elif(num == 2):
    print("Tuesday.")
elif(num == 3):
    print("Wednesday.")
elif(num == 4):
    print("Thursday.")
elif(num == 5):
    print("Friday.")
elif(num == 6):
    print("Saturdayy.")
else:
    print("Sunday.")