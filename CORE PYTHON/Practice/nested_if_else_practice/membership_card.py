#6. Write a Python program to check whether the purchase amount is greater than ₹5,000 and, if it is, check whether the customer has a membership card.
amount = int(input("Enetr the amount:"))

if(amount >= 5000):
    print("Purchase amount is greater than 5000rs.")
    if(amount > 5000):
        print("Customer has a membership card.")
    else:
        print("Customer not having membership card.")
else:
    print("Purchase amount is less than 5000rs.")