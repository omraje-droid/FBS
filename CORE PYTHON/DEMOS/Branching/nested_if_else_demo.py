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