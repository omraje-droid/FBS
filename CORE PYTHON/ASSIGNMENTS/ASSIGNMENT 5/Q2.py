#2. Enter number of students from user. For those many students accept marks of 5 subject marks from user and calculate percentage.
#  Display all percentage and average percentage of students.

student = int(input("Enter the number of student:"))
total= 0

for i in range(1,student+1):

    sum = 0

    for j in range(1,6):
        
        marks=int(input("Enter the marks:"))
        sum += marks


        total += sum 
    percentage = total / 5
    print(f"student {i} having percentge {percentage}") 

average = percentage / student

print(f"Average percentage of student {student} is {average} ")



