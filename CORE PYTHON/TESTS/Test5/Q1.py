li = [ 2000 ,500 , 200 , 100 , 50 ,20 ,10 ,5]
total_notes = 0
amount = int(input("Enter amount:"))
for i in li:
    count = amount // i
    amount = amount % i

    if count > 0:
        print(i,":",count,"notes")

    total_notes = total_notes + count
print ("Minimun number of notes:" , total_notes)