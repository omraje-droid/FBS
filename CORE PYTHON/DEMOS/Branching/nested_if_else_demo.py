#In nested if else ther are multiple conditon of if else
#Dependancy:
#nested if else next condition will depended on previous condition by tru or false.
#nested if else having true or false structure.
#multiple condition are true in the nested if else.

gender = input("Enter the gender M/F:")
age = int(input("Enter the age:"))

if(gender == 'M'):
    if(age >= 21):
        print("Boy is elegible for marriage.")
    else:
        print("Not elegible for marriage.")
else:
    if(age>=18):
        print("Girl is elegible for marriage.")
    else:
        print("Girl is not elegible for marriage.")