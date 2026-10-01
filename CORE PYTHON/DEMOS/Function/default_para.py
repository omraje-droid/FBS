#1. To make parameter optional . 
#2. Assign valu to parameter in  function definition.
#3. If we pass value to default parameter , it take passed value .
 # If we don't pass value to default parameter , it take default value.
#4. Flow from right to left .


def emp(id , name , sal ,dep = "Bank Office"):
    print("ID:", id)
    print("NAME:", name)
    print("SALARY:",sal)
    print("DEPARTMENT:",dep)

emp(123,'ABC',456780)


print("******************************")


def state(id , name , sal , dep ):
    print("ID:", id)
    print("NAME:", name)
    print("SALARY:", sal)
    print("DEPARTMENT:",dep)

emp( 208 ,'OM',43562780,' IT')

print("################################")

def inf(id , name , sal =50000 , dep = 'Teacher'):
    print("ID:", id)
    print("NAME:", name)
    print("SALARY:" , sal)
    print("DEPARTMENT:", dep)

inf(890 ,'OMRAJE')


# we can not create the optional in between the series .
# like def om(id , name = "omraje " , sal , dept = 'Student').
# Its gives error because the function call will perform process like one by one value. 
# IF function call having valuw like om(1242 , 5000).
# It give the 5000 value to name not for the sal. 

#Flow from right to left means the functionName parameter give the option values from right to left only .
#Flow from left to right means the function call parameters will run or give the values from left to right. 