#3. Accept no. of passengers from user and per ticket cost. 
# Then accept age of each passenger and then calculate total amount to ticket to travel for all of them based on following condition :
#a. Children below 12 = 30% discount
#b. Senior citizen (above 59) = 50% discount
#c. Others need to pay full.

passenger = int(input("Enter number of passengers:"))

ticket_cost =int(input("Enter the tickert cost:"))

total = 0

for i in range(1,passenger+1):

    age = int(input("Enter age of each passenger:"))

    if(age < 12):
        cost = ticket_cost * 30/100

    elif(age > 59):
        cost = ticket_cost * 50/100

    else:
        cost = ticket_cost

    print(cost)
    total += cost
print(f" {passenger} passenger gets total amount : {total}")    


