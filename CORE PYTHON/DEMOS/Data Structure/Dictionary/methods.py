di = {1:"python" , 2:"java" ,3:"C"}

#di .clear() # it will remove all .

di.copy() # used to copy 

Di= di .get(4) # it returns none because defult parameter.
Di = di.get(4,'key not present')
print(Di)

print(di.items())

print(di.keys())

print(di.pop(2)) # for removing the key from the dictionary or elelment

print(di.popitem()) # for remove the last element.

di.update({4:"PHP" , 5:"R"}) #for add the element.
print(di)

print(di.values()) # only returns the value.

