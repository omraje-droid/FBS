#1. To reduce lines of code
#2. Perform same task  multiple time on diff input 

#list is used for store multiple data at a time .

def sq(n):
    return n * n

data  = [1,2,3,4,5,6,7,8,9,10]

# method 1

res = list(map(sq,data))
print(res)


# method 2 

res = list(map(lambda n : n*n , data))

print(res)