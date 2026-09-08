# Data_Type:-

# Datatype means which type of data will stored in variable

###### 1) Numaric:-

# Numaric is not a datatype .
# Numaric is category of datatype

# 1) int:-

# int means integer ,integer means whole numbers without decimal point. 
# int stores whole numbers only.

#int var  #variable declaration in different language

var = 10  #variable initialization
print(type(var))

#output:- <class 'int'> 

# we see in output only the value type will print 10 in output.
# print(type(var)) is used to get which type of will give by user.
# python is a dynamic typing because variable can hold differnt types of value.
# In python we can give the values diect to the variable can't declare the datatype in python.
 
# 2) float:-
var=234.098
print(type(var))

#float means decimanl number not whole number

#3) complex:-
var= 10 + 5j
# 5j is imaginary part
# 10 is a real part
# in python j will used for imaginary & in other language i will used in complex
print(type(var))


##### 2) Text:-
#string:-
var="Om Deshmanre"
print(type(var))
#Double Quotes
#var="OM DESHMANE"

#Single Quotes
#var='Om deshamne'

#multi line string having ''' Quotes at starting and ending '''

#comment :- cann't translate in binary and does not exectued in python \
# (#) is used for the comment in python 
# ('''  ''') we also knows multiple line comment we can write in thim but it is not a multiple line comment this is S string like structure its not comment like writing process
#when we write the var= '''__ ''' its goes in string ;like structure only (#) is used for comment

####### 3) Sequential

#1) list
var=[10, 20, 30, 40 ]  #values writen in Square Brackets
print(type(var))

#2) tuple
var=(10, 20, 30, 40)  #values writen in Round Brackets or Parentheses
print(type(var))

#3)range()
var = range(1,51)   #this is used for generate the values from range 1 to 50.
print(type(var))
print(var)

##### 4) SET TYPES

#1) set
var = {10, 20, 30 ,40}  #values in curly brackets.
print(type(var))

#2) forzenset
var = frozenset({10, 20 , 30, 40}) #first is round brackets ,second is curly brackets in both brackets vqalues in between the curly brackets.
print(type(var))


###### 5)Mapping

#1)Dictinory (dict)
var = {1:'python', 2:'Java', 3:'c'} # values are in curly bracket in pattern like key : value
print(type(var))
# (:) this is called colon 
# left side of colon is key.
# right side of colon is value.

###### 6) Other 

#1) boolean
var = True 
print(type(var))
# Boolen having two types only True or False

#2) Nonetype
var = None
print(type(var))

#none mean "no value " or "nothing"
#Example:-
x = None
print(x)