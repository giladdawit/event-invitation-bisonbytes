#Merge Sort
def merge_sort_ascending(data):
    if len(data) <= 1:
        return data
        
    mid = len(data)//2
    left = merge_sort_ascending(data[:mid])
    right = merge_sort_ascending(data[mid:])

    return merge_ascending(left, right)

def merge_ascending(left, right):
    results = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            results.append(left[i])
            i += 1
        else:
            results.append(right[j])
            j += 1
    
    results.extend(left[i:])
    results.extend(right[j:])
    return(results)
data = [38, 27, 43, 3, 9, 82, 10]

sorted_data = merge_sort_ascending(data)
print("Ascending order:", sorted_data)


#Quick Sort

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
     
    return quick_sort(left) + [pivot] + quick_sort(right)

data = [38, 27, 43, 3, 9, 82, 10]

# Sort the data in ascending order
sorted_data = quick_sort(data)
print("Ascending order:", sorted_data)

       
#Binary search tree

def inorder