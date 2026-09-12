#2.Write a program to input any alphabet and check whether it is vowel or not.

alphabet =input("Enter the aplhabet:")
vowels = ('a','e','i','o','u','A','E','I','O','U')
if(alphabet in vowels):
    print("Given alphabet is vowel.")
else:
    print("Given alphabet is not vowel.") 