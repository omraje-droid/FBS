# how to find the fibonacci number.
n = int(input("How may fibonacci number you want: "))

a = -1
b = 1

for i in range (n):
    c = a + b
    print(c, end = ' ') #( end = ' ' ) this is used for get the output in one line or not get output in next line.
    #( end = ' ' ) is only used in print function at end of our output .
    a = b
    b = c 