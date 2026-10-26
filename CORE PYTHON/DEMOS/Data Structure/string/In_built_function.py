s = ' hi i am om'
upsc = s.upper() # convert all string into capital letter.

print(s.title()) # convert only first letter into capital letter.

print(upsc.capitalize())
print(s.capitalize()) # convert the capital letter into small.

s = "PYHTON java"
print(s.swapcase()) # convert the small letter into capital letter.

# searching method.

#1. find()
str = ("Good in Python")

#It retuns the startingindex of sentence or letter.

#5. count()
#It will print the count of matching string .
#If not found then it will retun 0

str = ("Good in python Good")

print(str.count("Good"))
print(str.count("java"))
print(str.count("good"))


str = "I love java java java"
print(str.replace('java','python'))
print(str.replace("java","pyhton",2))

