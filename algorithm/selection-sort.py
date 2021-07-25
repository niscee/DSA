arr = [7,3,1,6,9,12,4]

def filterOut(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if smallest > arr[i]:
            smallest = arr[i]
            smallest_index = i
    return smallest_index




def selectionsort(arr):
    newArr = []
    for i in range(len(arr)):
        res = filterOut(arr)
        newArr.append(arr[res])
        del arr[res]
    return newArr





result = selectionsort(arr)
print(result)
