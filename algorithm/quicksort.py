def partitioning(array, low, high):
    pivot = array[high]

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # if element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
        print("swap: ")
        print(array)
   
    # swap the pivot element with the greater element specified by i
    array[i + 1], array[high] = array[high], array[i + 1]

    # return the position from where partition is done
    return i + 1



def quickSort(arr, low, high):
    if low < high:
        p = partitioning(arr, low, high)
    
        #partitioning for left side.
        quickSort(arr, low, p-1)

        #partitioning for right side.
        quickSort(arr, p+1, high)





data = [7,2,1,8,6,3,5,4]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)
