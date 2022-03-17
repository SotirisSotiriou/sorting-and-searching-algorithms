from random import randint


#set order asc or desc

def insertionSort(array, order='asc'):
    if order == 'asc':
        for step in range(1, len(array)):
            key = array[step]
            j = step - 1
            
            # Compare key with each element on the left of it until an element smaller than it is found
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j = j - 1
            
            # Place key at after the element just smaller than it.
            array[j + 1] = key
    elif order == 'desc':
         for step in range(1, len(array)):
            key = array[step]
            j = step - 1
        
            # Compare key with each element on the left of it until an element greater than it is found
            while j >= 0 and key > array[j]:
                array[j + 1] = array[j]
                j = j - 1
            
            # Place key at after the element just greater than it.
            array[j + 1] = key
    else:
        print("Wrong order type!")
        return array
    return array



def selectionSort(array, order='asc'):
    if order == 'asc':
        for step in range(len(array)):
            min_idx = step;
            #find index of the min element in subarray
            for i in range(step+1, len(array)):
                if array[i]<array[min_idx]:
                    min_idx = i;
            
            #swap min element with step element
            (array[step], array[min_idx]) = (array[min_idx], array[step])
        return array
    elif order == 'desc':
        for step in range(len(array)):
            max_idx = step;
            #find index of the min element in subarray
            for i in range(step+1, len(array)):
                if array[i]>array[max_idx]:
                    max_idx = i;
            
            #swap min element with step element
            (array[step], array[max_idx]) = (array[max_idx], array[step])
        return array
    else:
        print("Wrong order type!")
        return array


def bubbleSort(array, order='asc'):
    if order == 'asc':    
        # loop to access each array element
        for i in range(len(array)):

            # loop to compare array elements
            for j in range(0, len(array) - i - 1):

                # compare two adjacent elements
                if array[j] > array[j + 1]:

                    # swapping elements if elements
                    # are not in the intended order
                    temp = array[j]
                    array[j] = array[j+1]
                    array[j+1] = temp

    elif order == 'desc':
        # loop to access each array element
        for i in range(len(array)):

            # loop to compare array elements
            for j in range(0, len(array) - i - 1):

                # compare two adjacent elements
                if array[j] < array[j + 1]:

                    # swapping elements if elements
                    # are not in the intended order
                    temp = array[j]
                    array[j] = array[j+1]
                    array[j+1] = temp

    else:
        print("Wrong order type!")
    
    return array


def __merge(left, right, order='asc'):
    # If the first array is empty, then nothing needs
    # to be merged, and you can return the second array as the result
    if len(left) == 0:
        return right

    # If the second array is empty, then nothing needs
    # to be merged, and you can return the first array as the result
    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    # Now go through both arrays until all the elements
    # make it into the resultant array
    while len(result) < len(left) + len(right):
        # The elements need to be sorted to add them to the
        # resultant array, so you need to decide whether to get
        # the next element from the first or the second array

        #for ascending order
        if order == 'asc':
            if left[index_left] <= right[index_right]:
                result.append(left[index_left])
                index_left += 1
            else:
                result.append(right[index_right])
                index_right += 1

        #for descending order
        elif order == 'desc':
            if left[index_left] >= right[index_right]:
                result.append(left[index_left])
                index_left += 1
            else:
                result.append(right[index_right])
                index_right += 1

        # If you reach the end of either array, then you can
        # add the remaining elements from the other array to
        # the result and break the loop
        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result


def mergeSort(array, order='asc'):
    if not (order == 'asc' or order == 'desc'):
        print("Not right type of order, please select 'asc' or 'desc'")
        return array

    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(array) < 2:
        return array

    midpoint = len(array) // 2

    # Sort the array by recursively splitting the input
    # into two equal halves, sorting each half and merging them
    # together into the final result
    return __merge(left=mergeSort(array[:midpoint], order=order), right=mergeSort(array[midpoint:], order=order), order=order)



def quickSort(array, order='asc'):
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if not (order == 'asc' or order == 'desc'):
        print("Not right type of order, please select 'asc' or 'desc'")
        return array

    if len(array) < 2:
        return array

    low, same, high = [], [], []

    # Select your `pivot` element randomly
    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        # Elements that are smaller than the `pivot` go to
        # the `low` list. Elements that are larger than
        # `pivot` go to the `high` list. Elements that are
        # equal to `pivot` go to the `same` list.
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    # The final result combines the sorted `low` list
    # with the `same` list and the sorted `high` list
    
    #for ascending order
    if order == 'asc':
        return quickSort(low, order) + same + quickSort(high, order)

    #for descending order
    elif order == 'desc':
        return quickSort(high, order) + same + quickSort(low, order)



