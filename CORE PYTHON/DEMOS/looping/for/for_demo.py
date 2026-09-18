#synatx:
#for variable in iterable:
    #Block of code

#for loop is use for the  list, range, set, frogenset ,etc.
#for loop will execute the iterable in given range or list.


#what :- A for loop is used to repeat a block of code for each item in a sequence or range.
#why :- We use a for loop when we want to repeat something multiple times without writing the same code again and again.
#How :-
#for       → keyword
#i         → loop variable
#in        → takes values from
#range()   → generates numbers

li = [10, 20 ,30, 40, 50] #variable initalization
for ele in li:            #variable is used in condition & ele will get the iterate from li(list)
    print(ele)