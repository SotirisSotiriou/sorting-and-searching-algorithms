
import math


import math
from numpy import array


def linearSearch(array, element):
    for i in range(len(array)):
        if array[i] == element:
            return True, i
    return False, -1

#works in sorted arrays
def binarySearch(array, element):
    left = 0
    right = len(array)-1

    # Check base case
    if right >= left:
 
        mid = left + (right - left) // 2
 
        # If element is present at the middle itself
        if array[mid] == element:
            return True, mid
 
        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif array[mid] > element:
            return __subBinarySearch(array, element, left, mid-1)
 
        # Else the element can only be present
        # in right subarray
        else:
            return __subBinarySearch(array, element, mid + 1, right)
 
    else:
        # Element is not present in the array
        return False, -1

def __subBinarySearch(array, element, left, right):
    # Check base case
    if right >= left:
 
        mid = left + (right - left) // 2
 
        # If element is present at the middle itself
        if array[mid] == element:
            return True, mid
 
        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif array[mid] > element:
            return __subBinarySearch(array, element, left, mid-1)
 
        # Else the element can only be present
        # in right subarray
        else:
            return __subBinarySearch(array, element, mid + 1, right)
 
    else:
        # Element is not present in the array
        return False, -1


def jumpSearch( array , x):
    n = len(array)

    # Finding block size to be jumped
    step = math.sqrt(n)
     
    # Finding the block where element is
    # present (if it is present)
    prev = 0
    while array[int(min(step, n)-1)] < x:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return False, -1
     
    # Doing a linear search for x in
    # block beginning with prev.
    while array[int(prev)] < x:
        prev += 1
         
        # If we reached next block or end
        # of array, element is not present.
        if prev == min(step, n):
            return False, -1
     
    # If element is found
    if array[int(prev)] == x:
        return True, prev
     
    return False, -1