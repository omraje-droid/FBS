li = [40 ,50 ,40 ,60 ,70,[80,90],100]

li.append(110) # add the element in list . multiple element will added as single element.

li.clear()  #clear the list at a time

# deepcopy & shallowcopy (nested list) difference .// interview Question.

li = [40 ,50 ,60, [70 ,80, 90]]
li2 = li.copy()  # copy the list.

li[3][2] = 92

print(li)
print(li2)

li.count(40) # count how many same element will present

li.extend([70,80]) #extend works as multiple element will individually added in list.

# print(li.index(80)) # gives the value error not index error. 
# we pass the value in index not index like 0,1,2,3,4 of value.

li.index(40)  # check the index of value .

li.insert(1,90) # insert he value in the list.

li.pop() # remove the value from list if any index or value will noy give he removes last value.

print(li.remove(50)) # for removing value from list we use removing method

print(li.reverse())


li = [20,10,40,50,67,92,90,80]

li.sort()

li.sort(reverse = True)

print(li)
