#2.Write a program to input any alphabet and check whether it is vowel or consonant. 
alphabet = input("Enter the alphabet:")
vowels = ('a','e','i','o','u','A','E','I','O','U')
# by if else ladder.
if(alphabet in vowels):
    print("Given alphabet is vowels.")
elif('a'<= alphabet <='z')or('A'<= alphabet<='Z'):
    print("Given alphabet is consonant.")
else:
    print("Invalid character")
