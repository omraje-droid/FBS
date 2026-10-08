#Second max number in list.

li = [45 ,60 ,58 ,50 ,90 ,89]

max = li[0]
smax = 0 

for ind in range(1 , len(li)):
    if(li[ind] > max):  
        smax = max
        max = li[ind]

    elif(li[ind] > smax):
        smax = li[ind]

print('Max :',max)
print('Smax :', smax)
