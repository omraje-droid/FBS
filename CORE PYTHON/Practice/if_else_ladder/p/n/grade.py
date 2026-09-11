#2. Write a Python program to accept marks and display the student's grade based on the marks.


marks = float(input("Enetr the marks :"))

if(marks > 75):
    print("Student grade is (A+).")
elif(marks > 50):
    print("Student grade is (B+).")
elif(marks >= 35):
    print("Student grade is (C+).")
else:
    print("Student is not passed")