#bubble sort method

def bubbleSort (li):
    size = len(li)

    for i in range(size):
        for j in range(0,size-1):
            if(li[j] > li[j+1]):
                li[j] , li[j+1] = li[j+1] , li[j]
              #  print(f"\n{li}")
              #  print(i)

li = [50,40,30,20,10]

print("Before Sorting:",li)
bubbleSort(li)

print("After Sorting:",li)