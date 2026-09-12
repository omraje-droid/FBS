#10. Write a Python program to check whether a product is available in stock and,
# if available, check whether its price is within the customer's budget

product = input("Enter the name of product:")
stock = input("Enter the stock is avilable (Yes/No):")
prise = int(input("Enter the prise of product:"))
budget = int(input("Enter the budget :"))

if stock == "Yes":
    print("product is avilable in stock.")
    if(budget >= prise):
        print("product in customer's budget.")
    else:
        print("product is not in customer's budget.")
else:
    print("product is not avilable in stock")