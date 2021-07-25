arr = [7,3,1,6,9,12,4]

def insertion(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j+1] = key
    
    return arr    









result = insertion(arr)
print(result)
