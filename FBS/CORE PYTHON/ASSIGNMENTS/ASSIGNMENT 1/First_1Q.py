# Q. Write a program to calculate the percentage of student based on marks of 5 subject?

English=int(input("English Marks:"))
Math = int(input("Math Marks:"))
Physics = int(input("Physics Marks:"))
Chemistry = int(input("Chemistry Marks:"))
Biology = int(input("Biology Merks:"))

Total_Marks = 500
Obtained_Marks = English + Math + Physics + Chemistry + Biology

# Percentage of 5 subject marks

Percentage = (Obtained_Marks/Total_Marks)*100
print("Percentage of 5 subject marks :",Percentage)