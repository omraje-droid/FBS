#1. structure: [] 

li = [10 ,20 ,30 , 40 ]
print(type(li))
print(li)

#2 .Type of data :

li = [10 ,20 ,'abc' , 3.45]
print(li)
#It means different types of data stored.(Heterogenous)

#3 .Sequential :

li = [10 ,20 ,30 ,40, 3.04 , 'ABC']
print(li)

#ordered: sequence of element will be maintained

#4 .Changable:
print(id(li))
li[0] = 50
print(id(li)) 

#5 .Duplication: Allowed

# Duplication means one element store multiple time. 