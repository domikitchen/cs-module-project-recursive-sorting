# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    if len(arr) > 0:
        midpoint = (end + start) // 2
        if arr[midpoint] == target:
            return midpoint
        elif arr[midpoint] < target:
            return binary_search(arr, target, end, (midpoint + 1))
        elif arr[midpoint] > target:
            return binary_search(arr, target, (midpoint - 1), start)
        else:
            return -1
    else:
        return -1

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass

