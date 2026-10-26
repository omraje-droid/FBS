s = { 19,30,29,490,490}


#add
s.add(123)
print(s)

#update[]

s.update([12,34,56])
print(s)

#remove

s.remove(19)
print(s)

#discard

s.discard(1)
print(s)

#clear
s1 ={19 ,20 ,30, 40, 50 ,60 }

s1.clear()
print(s1)

#union

s2 = {1,3,4,7,9,3}
s3 = {12,2,4,6,8,10}
print(s2.union(s3))

#intersection

print(s2.intersection(s3))

#difference

print(s2.difference(s3))
print(s3.difference(s2))