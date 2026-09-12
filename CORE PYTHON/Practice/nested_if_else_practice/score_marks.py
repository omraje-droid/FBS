#3. Write a Python program to check whether a student has passed and, if passed, check whether the student has scored distinction marks.

marks = int(input("Enter the student marks:"))

if(marks>35):
    print("Student passed.")
    if(marks>75):
        print("Student has scored distinction marks.")
    else:
        print("student has not scored distinction marks.")
else:
    print("student not passed.")