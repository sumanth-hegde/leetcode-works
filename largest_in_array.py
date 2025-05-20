def largest_element(arr):
    largest = arr[0]
    for i in range(len(arr)):
        if arr[i] > largest:
            largest = arr[i]
    return largest


print(largest_element([2,3,5,2,1,9]))