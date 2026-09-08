#3. Convert distant given in feet and inches into meter and centimeter.
feet = float(input("Enter the feet value :"))
inches = float(input("Enter the inche values :"))

# converting feet into inches
inche = feet * 12

# Additoin of total inches
total_inches = inche + inches

# converting total_inches into centimeter

cm = total_inches * 2.54 

# converting centimeter into meter

m = (cm /100) 
print(f"Converted distant given in feet {feet} into inches {inche}.")
print(f"Converted total inches {total_inches} into centimeter {cm}.")
print(f"Converted cemtimeter {cm} into meter {m}.")
