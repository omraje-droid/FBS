#1. To pass the multiple values with meaning.
#2. Mention 2 asterisk symbols before para name in function definition.
#3. values & meaning stored in dictionary format.
#4. Use for loop on dict.items() to iterate data.

def emp (** data):
    for val in data:
        print(val)

emp(id=1234 , name='ABC' , sal=1500 , dept='IT')
# we see in output when dictionary will directly access then it gives only the meaning of each iteration not value also .

print("____________")

def emp (** data):
    for val in data.items():
        print(val)

emp(id=1234 , name='ABC' , sal=1500 , dept='IT')
# Her output data type is tuple .

print("____________")

def emp (** data):
    for key,val in data.items():
        print(key,":",val)

emp(id=1234 , name='ABC' , sal=1500 , dept='IT')
# Her output data type is dictionay .

#In for loop we use the  1 or more variable but when we get the constant value in iteration .