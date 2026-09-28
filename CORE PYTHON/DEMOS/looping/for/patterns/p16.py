for i in range (1,7):
    for j in range (1,7):
        if(i==1 or j == 1 or j == 6 or i == 6):
            print("*", end =' ')
        else:
            print((i+j)-1 , end =' ')

    print()

#2 code for same pattern

no = int(input("Enter the range :"))

for i in range(no):
    for j in range(no):
        if(i == 0 or i == no-1 or j == 0 or j == no-1):
            print("*", end =' ')
        else:
            print(i+j+1 , end=" ")
    print()