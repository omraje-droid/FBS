#11. Accept age of five people and also per person ticket amount and then calculate total
#amount to ticket to travel for all of them based on following condition :
#a. Children below 12 = 30% discount
#b. Senior citizen (above 59) = 50% discount
#c. Others need to pay full.

total = 0
for i in range(5):
    age = int(input("Enter the age:"))
    ticket = float(input("Enter the ticket amount:"))


    if(age < 12):
        discount = (30/100)*ticket
        amount = ticket - discount
        print("Ticket amount for children :",amount)
    else:
        if(age > 59):
            dis = (50/100)*ticket
            amounts = ticket - dis
            print("Ticket amount for senior citizeen:",amounts)
        else:
            print("person want to pay full amount",ticket)

    total = total + ticket
print("Total ticket amount :", total)