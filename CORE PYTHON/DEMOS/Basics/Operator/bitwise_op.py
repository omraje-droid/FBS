#Bitwise operator is always works on binary number (0s & 1s).

#1) Bitwise and (&):-
#               In bitwise (&) you get the output true if both are bits are true other wise false.

print(10 & 12)
#____________
# | T | T | 1 |
# | T | F | 0 |
# | F | T | 0 |
# | F | F | 0 |
# |___|___|___|
#                                             <----------
#Binary number in like                     32 16 8 4 2 1
#                                   10           1 0 1 0
#                                   12           1 1 0 0
#                    
#                              Ans: 8            1 0 0 0 


#2)Bitwise or (|):-
#                  In bitwise (|) you can get the output true when if any one is True. 
#                  Also we can say both are False then output is false.
print(36 | 14)
#   ___________
# | T | T | T |
# | T | F | T |
# | F | T | T |
# | F | F | F |
# |___|___|___|
#Binary number line                  32 16 8 4 2 1
#                              36     1  0 0 1 0 0
#                              14     0  0 1 1 1 0
#                          
#                          Ans:46     1  0 1 1 1 0  
#


#3)Bitwise XOR (^):-
#                  In bitwise XOR both bits are same output is False otherwise True.
#
print(16^21) 
#  ___________
#| T | T | F |
#| T | F | T |
#| F | T | T |
#| F | F | F |
#|___|___|___|
#
#Binary numbers line                       32 16 8 4 2 1
#                               16             1 0 0 0 0
#                               21             1 0 1 0 1 
#
#                           Ans:5              0 0 1 0 1
# 
 

#4)Negation (~):- (once complement)
# Once is used for change the True to False and False to true
# In negation will apply the on like -1*10 in your language we get -10 but 
# whan we use the negation to any number like ~10 he give -11 because the pyhton calculate as 1*(10+1)
print(~19)
print(~10)
print(10)





#5)Bitwise left shift(<<):

print(10<<2)


#          32 16 8 4 2 1
#        
#     10 =       1 0 1 0
#                | | | |
#           1<---- | | |
#              0<--- | |
#                 1<-- |
#                    0<-
# ________________________
#    40 =    1 0 1 0 0 0





#6) Bitwise right shift(>>):

print(15>>2)


#           32 16 8 4 2 1
#
#   15 =          1 1 1 1
#                 | | | |
#                 | | |  ------>1 goes from range to calculate.
#                 | | --------->1 goes from range to calculate. 
#                 | --->1
#                 ---->1
#__________________________
#  3 =            0 0 1 1