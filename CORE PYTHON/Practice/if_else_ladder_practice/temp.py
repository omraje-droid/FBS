#7.Write a Python program to accept a temperature and display whether the weather is cold, normal, warm, or hot.
temp = int(input("Enter the temperature:"))
if(temp <= 16):
    print("Temperature is cold ")
elif(temp <= 25):
    print("Tempearture is normal.")
elif(temp <= 35):
    print("Temperature is warm.")
else:
    print("Temperature is hot.") 