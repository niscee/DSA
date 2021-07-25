def smallestVal(arr):
    if len(arr) == 1:
        return arr[0]

    return min(arr[0], smallestVal(arr[1:]))    




