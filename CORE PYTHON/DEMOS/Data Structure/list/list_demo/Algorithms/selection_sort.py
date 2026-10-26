# Selection Sort :-

# In selection sort we get the first element then comapre with all and then replace.

def selectionSort(li):
    size = len(li)
    for i in range(0,size-1):
        min_ind = i
        for j in range(i + 1 , size):
            if(li[j] < li[min_ind]):
                min_ind = j
        li[i] , li[min_ind] = li[min_ind] , li[i]
        print("\n",li)

li = [60 ,50, 40, 30, 20, 10]

print("Before sorting", li)
selectionSort(li)

print("After sorting", li)