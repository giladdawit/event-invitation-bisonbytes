# Sort Grades in Descending Order Using Merge Sort
def merge_sort_descending(grades):
    if len(grades) <= 1:
        return grades
    
    mid = len(grades) // 2
    left = merge_sort_descending(grades[:mid])
    right = merge_sort_descending(grades[mid:])

    return merge_descending(left, right) # type: ignore

def merge_descending(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i][1] > right[j][i]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[i])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

sorted_grades= merge_sort_descending(grades_list):
print("Descending Order:", sorted_grades)

