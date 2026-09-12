#2.Write a program to input any alphabet and check whether it is vowel or consonant. 
alphabet = input("Enter the alphabet:")
vowel =('a','e','i','o','u','A','E','I','O','U')

if('a'<= alphabet <='z' or 'A' <= alphabet <= 'Z'):
    if(alphabet in vowel):
        print("Given alphabet is vowel.")
    else:
        print("Given alphabet is consonant.")
else:
    print("Invalid character.")