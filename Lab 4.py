def merge_sort_ascending(grades):
    if len(grades) <= 1:
        return grades
    
    mid = len(grades) // 2
    left = merge_sort_ascending(grades[:mid])
    right = merge_sort_ascending(grades[mid:])

    return merge_ascending(left, right)  

def merge_ascending(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i][1] <= right[j][1]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1  
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

Grades = {
    'Charles': 100, 'Chris': 85, 'Ema': 60, 'Ariel': 65, 'John': 85,
    'Patrick': 55, 'Stella': 50, 'Sharon': 89, 'Victoria': 83, 
    'Debby': 90, 'Suzanne': 78, 'Kevin': 76
}

grades_list = list(Grades.items())

sorted_grades = merge_sort_ascending(grades_list)
print("Ascending Order:", sorted_grades)



# Sort Grades in Descending Order Using Merge Sort
def merge_sort_descending(grades):
    if len(grades) <= 1:
        return grades
    
    mid = len(grades) // 2
    left = merge_sort_descending(grades[:mid])
    right = merge_sort_descending(grades[mid:])

    return merge_descending(left, right) 

def merge_descending(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i][1] >= right[j][1]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[i])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

sorted_grades= merge_sort_descending(grades_list)
print("Descending Order:", sorted_grades)


# Modify Ascending Sort to Handle Same Grades Alphabetically
def merge_sort_with_names(grades):
    if len(grades) <= 1:
        return grades  
    
    mid = len(grades) // 2
    left = merge_sort_with_names(grades[:mid])
    right = merge_sort_with_names(grades[mid:])

    return merge_with_names(left, right)  

def merge_with_names(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
       
        if left[i][1] < right[j][1] or (left[i][1] == right[j][1] and left[i][0] < right[j][0]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1  

    result.extend(left[i:])
    result.extend(right[j:])  
    return result


Grades = {
    'Charles': 100, 'Chris': 85, 'Ema': 60, 'Ariel': 65, 'John': 85,
    'Patrick': 55, 'Stella': 50, 'Sharon': 89, 'Victoria': 83, 
    'Debby': 90, 'Suzanne': 78, 'Kevin': 76
}

grades_list = list(Grades.items())

sorted_grades_with_names = merge_sort_with_names(grades_list)
print("Ascending Order with names:", sorted_grades_with_names)