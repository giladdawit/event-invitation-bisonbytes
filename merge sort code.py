#Function to merge two sorted subarrays

def merge(name, grade):
    sorted_array = []
    i = j = 0        #i: Tracks the current position in the left subarray.
                     #j: Tracks the current position in the right subarray

#Compare elements from both subbarrays and merge them

    while i <len(left) and j < len(right):
         if left[i] < right[j]:
             sorted_array.append(left[i])
             i += 1
         else:
             sorted_array.append([j])
             j += 1
    
#Collect remaining elements from the left and right arrays

    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])

    return sorted_array



