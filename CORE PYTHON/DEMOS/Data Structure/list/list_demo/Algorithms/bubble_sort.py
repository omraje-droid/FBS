#bubble sort method

# we seen in bubble sort we swap element to sort the list.
# we use two loop outer loop or inner loop.
# outer loop work as n-1 means (length of list - 1 ) and change when the inner loop completer there all range.
# inner loop work to compare the element by using if . 



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