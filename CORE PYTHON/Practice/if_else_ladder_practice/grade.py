#2. Write a Python program to accept marks and display the student's grade based on the marks.

marks = int(input("Enter the student marks:"))

if (marks >= 75):
    print("Student gets A+ grade.")
elif(marks>=50):
    print("Student gets B+ grade.")
elif(marks>=35):
    print("Student get C+ grade.")
else:
    print("Student not passed.")