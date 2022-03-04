
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

