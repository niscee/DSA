def moveElementToEnd(array, toMove):
    i = 0
    j = len(array) - 1
    while i < j:
        if array[i] == toMove:
            array[i], array[j] = array[j], array[i]	 
            j -= 1
        else:
            i += 1

    return array                   

        


result = moveElementToEnd([2, 1, 2, 2, 2, 3, 4, 2], 2)
print(result)





""" 

1, 2, 3, 4, 2, 2, 2, 2


"""
 

