# Indexing :- 

# 1. positive index:
# positive index start from "0"

# 2. negative index:
# negative index start from "-1"

# (li) is list will writen in python.

# Why we not start negative index with "0"?
# -> Because positive index start also from zero and if we can start positive or negative both from " 0 " then they will not give elemeant 2 element can getted the same index number zero.\
# so we can start positive from "0" and negative from "-1".

li = [10 ,20 ,30, 40, 50, 60]

#for getting the 30 value we can print as

print(li[2])

#li[index] this is a syntax to print the value of given index.

## iterable is a container .
## variable is not a container its an identifier.

# if we want the length of a list means how many values in list .
# for finding the lenght to get the total or for finding the last (value / element) using the index

# we use " len(li) " as a syntax to find the length of list

print(len(li))

# we want to find the last element by using only positive index so we subtract the length of list with 1

# we use " li[len(li)-1] " this syntax gives the last (elemant / value).

li = [1 , 2, 3, 4, 5, 6, 7, 8, 9, 10, 40]
print(len(li)) 
print(li[len(li)-1])

#for negative indexing we get from -1
# i want the -2 position element.


print(li[-2])