#5. WAP to calculate selling price of book based on cost price and discount.
c_p = int(input("Enter the cost prise of book :"))
dis = int(input("Enter the discount on book :"))

# calculate discount prise

d_p = (c_p * dis)/100

# calculate selling prics 
s_p = c_p - d_p

print("Enter the discount prise on book",d_p)
print("Enter the selling prise of book",s_p)