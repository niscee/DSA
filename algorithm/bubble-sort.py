arr = [7,3,1,6,9,12,4]

def bubblesort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


    return arr           









result = bubblesort(arr)
print(result)
