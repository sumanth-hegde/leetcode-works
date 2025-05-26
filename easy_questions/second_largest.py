def second_largest_element(arr):
    largest = arr[0]
    second_largest = -1
    for i in range(len(arr)):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
        elif largest > arr[i] > second_largest:
            second_largest = arr[i]
    return second_largest

def second_smallest_element(arr):
    smallest = arr[0]
    second_smallest = 0
    for i in range(len(arr)):
        if arr[i] < smallest:
            second_smallest = smallest
            smallest = arr[i]
        elif arr[i] != smallest and arr[i] < second_smallest:
            second_smallest = arr[i]
    return second_smallest


print("Second largest : ",second_largest_element([3,4,1,6,2,7,250,205,177,9,249]))
print("Second smallest : ",second_smallest_element([3,4,1,6,2,7,250,205,177,9,249]))