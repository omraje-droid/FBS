#9. Input 5 subject marks from user and display grade(eg.First class,Second class ..) 

sub1 = int(input("Enter first subject marks:"))
sub2 = int(input("Enter second subject marks:"))
sub3 = int(input("Enter third subject marks:"))
sub4 = int(input("Enter forth subject marks:"))
sub5 = int(input("Enter fifth subject marks:"))

total_marks = 500
obtained_marks = sub1 + sub2 + sub3 + sub4 + sub5

percentage = (obtained_marks/total_marks)*100

if (percentage >= 75):
    print("First class")
elif(percentage >= 50):
    print("Second class")
elif(percentage >= 35):
    print("Third class")
else:
    print("Not Passed")