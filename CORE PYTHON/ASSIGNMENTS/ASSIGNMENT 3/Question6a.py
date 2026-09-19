#6. Write a program to calculate profit or loss.
c = int(input("Enter the cost prise:"))
s = int(input("Enter the selling prise:"))

p = s - c
l = c - s

if(p > l):
    print("Profit")
else:
    print("loss")