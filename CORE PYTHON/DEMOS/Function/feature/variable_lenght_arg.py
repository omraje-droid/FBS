# 1. To pass multiple parameters to function
# 2. Metions 1 asterisk before para name in function definition.
# 3. Values are stored in tuple format.
# 4. Use  for loop to iterate value individually from tuple.

def add(data):
    print('Function executed.')

add(10)
# add(10,20,30) when we get the multiple parameters then its gives error .

# 2. Metions 1 asterisk before para name in function definition.

print("######################################")
def add(*data):
   
    print(type(data)) # To find the data types of data 

    print("___________________")

    print("hello")

    print("^^^^^^^^^^^^^^")
add(10,20,30,40,50,60,70,2,3,4,5,6,7)

#we see only one star before parameter will added it will get multiple parameter from the function call (parameters values).

# for loop is used for get the one by one value from iterable .


# print() function get multiple parameters can get or display on Terminal .
# plus (+) is binary operator it's perform only two numbers addition . 

def add (*data):

    sum = 0

    for val in data:
        sum+=val
    return sum  # return function is used after the for loop because to return the next value of sum .
                # if we use the return functio in for loop then he returns the only first value .

print(add(10,20,30,40,50))

print("*******************")
res =add(10,20,30,40,50,60,70,80,90,100) 
print(res) #reutrn the value after addition 

# Why we use the res before the funcion call?
#-> The function call returns the final answer, and the res variable stores that answer when we write res = add(...).