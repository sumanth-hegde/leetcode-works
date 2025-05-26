def largest_element(arr):
    largest = arr[0]
    [largest := arr[i] for i in range(len(arr)) if arr[i] > largest]
    return largest


print(largest_element([2,3,5,2,1,9]))