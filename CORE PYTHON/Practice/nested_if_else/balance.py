#9 . Write a Python program to check whether a bank account has sufficient balance for withdrawal and,
#  if sufficient, check whether the withdrawal amount is within the daily limit

amount = int(input("Enetr the withdrawal ammount:"))

if(amount <= 5000):
    print("Balance is sufficent.")
    if(amount <= 3000):
        print("Daily limit was not corss.")
    else:
        print("You can't withdrawal this ammount.")
else:
    print("Balance is unsufficent.")
    