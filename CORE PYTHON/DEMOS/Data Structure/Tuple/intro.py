#1. structure = ()

tu = (90,40,50)

tu=(90) # it gives the int data type not tuple.
tu = (90,) # it gives data type tuple (,) will used becaues for not gat int data type it also says multiple values are there. 

tu = 10 , 20 ,30 ,40 ,50 # when we get the multiple vales by using (,) it will converted in tuple.

#2. Heterogenous data will stored:
tu = (10 ,20 ,3, 3.40 ,"abcd")

#3. Order collection:
#sequence of element is maintained.
tu = (10,20,30,40,50,60,7.9,"sdfg")
#sequence will not change when we print multiple time.


#4.tuple is immutable :

#tu[0] = 50
# tuple can not change her values.
# tuple having only two methods count or index.
# 
# count means how many time value will present in tuple.
# index means value in which index.

#5) duplication allowed.
# means we can write same values in tuple. 
tu = [10,20,20,30,40,50,606,66]
print(type(tu))
print(tu)