#while loop
#syntax:-
#while(condition):
    #Block of code

#loop executed when the condition will true,When conditon will become false loop will stop.
#Infinite
# If loop condition will continous true then it will infinite they not stop or brack.

#Variable dependancy for finite stage
# 1) variable initalization
# 2) variable used in condition
# 3) variable value should change      

#What :- A while loop repeatedly executes a block of code as long as a condition is True.
#Why :- We use while when we want to repeat something until a particular condition becomes False
#How :- 
#| Step | `i` | Condition `i <= 3` | Action  |
#| ---- | --: | ------------------ | ------- |
#| 1    |   1 | True               | print 1 |
#| 2    |   2 | True               | print 2 |
#| 3    |   3 | True               | print 3 |
#| 4    |   4 | False              | Stop    |



i = 0                        #variable initalization
while (i<=3):                 #variable used in condition
    print("Hello World!")
    i += 1                   #variable value should change



i=1
while(i<=3):
    print(i)
    i += 1