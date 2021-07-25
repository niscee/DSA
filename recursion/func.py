# nth fibonacci.
def getNthFib(n):
    if n == 2:
        return 1
    
    if n == 1:
        return 0


    return getNthFib(n-1) + getNthFib(n-2)  



# Write a recursive function that, given a number  n, returns the sum of the digits of the number n.
def sum(n):
    if n == 1:
        return 1

    return n + sum(n-1) 



# Write a recursive function that, given a string s, prints the characters of s in reverse order.
def reverseOrder(str):
    if len(str) == 1:
        return str

    return reverseOrder(str[1:]) + str[0]



# duplicate Zeros.
def duplicateZero(array):
    val = 0
    arrayLen = len(array)

    # edge case.
    if val not in array:
        return array
    
    i = 0
    while i < arrayLen-1:
        if array[i] == 0:
            j = arrayLen - 2
            while j >= i:
                array[j+1] = array[j]
                j -= 1

            i += 2 

        i += 1
        
    return array 





    
    
    






    
       









