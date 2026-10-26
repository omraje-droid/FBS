#dictionary means value of pairs.

#1. structure

# {} - curly brace

di = {}

# di = {10,20,30,} # it will gives set.

di = {1 : "python" , 2 : "java" , 3 : " c++"}
print(type(di))


#2. Hetrogenious 

#dictionary is a hetrogenious because different datatypes value will store.
di = {1 : " python" , 2 : "java" , 3 : 1234 , 4 : 23.34}

#3. Ordered :
#In Python 3.6, dictionaries maintained insertion order as an implementation detail in CPython, but it was not officially guaranteed by the Python language.
# “In Python 3.7, dictionaries maintain the insertion order of items.”

# dictionary is also called as customizable indexing.

# In dictionary indexing will not present.

#4. value : Mutable , size : mutable , 
# key is immutable .


di[5] = 78 # if the key will not exist the element will key or value will added.

di[3] = 24.78 # if the key will exist then value will change .

#5. key : unique , value : Duplicantion allowed.
di = {1:10 , 2 :50 , 3:60 , 1: 20}  #overwrite / update.
print(di)

