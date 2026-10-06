#Reduce line of code.
#Filter is used for filter the data.
#Filter works like data will pass to lambda will get data the check condition will false the data will not print. 


data =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

res = list(filter(lambda num : num % 2 == 0 , data))
print(res)


#res = list(filter(lambda n : n*n , data))
#print(res)


#Falsy value : False , 0 , None , Blank ,' ' , [] .