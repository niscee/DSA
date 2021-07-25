# binary search.

arr = [1,2,3,4,5,8,12]
findVal = 0


def binarySearch(arr, findVal):
    low = 0
    high = len(arr)-1

    while low < high:
        mid = (low + high)//2

        if findVal > arr[mid]:
            low = mid + 1

        if findVal == arr[mid]:
            return True


        if findVal < arr[mid]:
            high = mid - 1


    return False






result = binarySearch(arr, findVal)
print(result)