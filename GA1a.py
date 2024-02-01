
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
# l is for left index and r is right index of the
# sub-array of arr to be sorted
 
def mergeSort(arr, l, r):
    if l < r:
 
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2
 
        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
 
def binary_search_greater(num1, arr2, min, max, t_min):

 
    if (min <= max):
        m = (min + max)//2

        sum = num1+ arr2[m]

        if(sum >= t_min):

            minIndex = binary_search_greater(num1, arr2, min, m-1, t_min)
        
            if (minIndex < m):
                return minIndex
            else:
                return m
        else:
            minIndex = binary_search_greater(num1, arr2, m+1, (len(arr2)-1), t_min)

            return minIndex
        
    else:
        return (len(arr2)+1)
        
def binary_search_lesser(num1, arr2, min, max, t_max):

 
    if (min <= max):
        m = (min + max)//2

        sum = num1+ arr2[m]

        
        if(sum <= t_max):

            minIndex = binary_search_lesser(num1, arr2, m+1, max, t_max)
        
            if (minIndex > m):
                return minIndex
            else:
                return m
        else:
            minIndex = binary_search_lesser(num1, arr2, max, m-1, t_max)

            return minIndex
        
    else:
        return (-1)


def findMatch(num1, arr2, t_min, t_max):

    #print("NUM1:",num1)
    #Lower bound
    t_min - num1
    #13   - 4
    #9 Lowest 
    low = binary_search_greater(num1, arr2, 0, (len(arr2)-1), t_min)
    high = binary_search_lesser(num1, arr2, 0, (len(arr2)-1), t_max)

    high = high+1

    if (low != len(arr2)+1 and high != -1):
        combos =+ (high-low)
        
    return combos

    
    
def probA(arr1, arr2, t_min, t_max):

    n = len(arr1)
    m = len(arr2)
    
    #First mergeSort arrays O(nLog(n))
    mergeSort(arr1, 0, n-1)
    mergeSort(arr2, 0, m-1)

    #Second recursive call for each item in A
    count = 0

    for i in arr1:
        count += findMatch(i, arr2, t_min, t_max)

    print (count)

arr1 = [0,1,8]
#0,1,8

arr2 = [5,6,4]
#4,5,6

#0+5, 0+6, 0+4  3
#1+5, 1+6, 1+4  3
#8+5, 8+6, 8+4  2

#8+6 shouldn't work

t_min = 0
t_max = 14

probA (arr1, arr2, t_min, t_max)

# This code is contributed by Mohit Kumra

#-4+ 3 -> -1, not between 0-13
#So the index of 1 would be 4 which would be 0
# it works

#Prove nlogn for binary search

