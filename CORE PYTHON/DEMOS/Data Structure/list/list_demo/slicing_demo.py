#slicing will not return an error.
# It will reutrn values and it will not return values.

li = [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90 , 100]

#without getting the range
res = li[1:8:]

#without getting the starting range then he start from first value.
res = li[:8]

#without getting ending range then end range will the last value.
res = li[0:]

#for the revrse value.
res = li[8:0:-1]

#It work on any range at last to print all value
res = li[0:20]

#we can want whole list so we retun only two colon or one also

res = li[::] 
res = li[:]

# we can want revers of hole list 

res = li[::-1]  

print(res)