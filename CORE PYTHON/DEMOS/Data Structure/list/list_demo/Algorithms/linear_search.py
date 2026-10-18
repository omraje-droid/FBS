# use first function 
# create code in function 

def linearSearch(li,Search_ele):     #function 
    for i in range(0,len(li)):          #for loop i used to create a loop to find ele is present in which index.
        if (Search_ele == li[i]):           # if is used to compare ele is present on list or not .
            return i

    else:
        return -1

    

li = [10 ,20, 30, 40, 50 ,60, 70, 80 ,90 , 11 , 23 , 4, 57 ,3 , 2, 0, 1]
ele = int(input("Enter element to find:"))

res = linearSearch(li,ele)              # res is a veriable Which store the return value. when the function call to function defination .

# funtion call only returns the final answer variable (res) stores it.

if(res != -1):                                            # This if check the index is not equal to -1 or not .               
    print(f"{ele} is present at index {res} .")

else:
    print(f"{ele} is not present in list.")



# Time complaxity (O):

# 1. Best case : O(1)    // Means when we get the ele in frist time when we search.
# 2. Worst case : O(n)   // Means check all ele and get at last .\
# 3. Average case : O(n) // means also as wrost case .