# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):

    # Your code here
    merged_arr = []
    
    s = 0
    e = 0

    while s < len(arrA) and e < len(arrB):
        print(f"arrA: {arrA}  arrB: {arrB}")
        if arrA[s] < arrB[e]:
            print(f"  arrA: {arrA}")
            # merged_arr.pop(0)
            merged_arr.append(arrA[s])
            s += 1
        else:
            print(f"  arrB: {arrB}")
            # merged_arr.pop(0)
            merged_arr.append(arrB[e])
            e += 1

    merged_arr += arrA[s:]
    merged_arr += arrB[e:]

    print(f"merged boi:{merged_arr}\n")
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    middy = len(arr) // 2
    start = merge_sort(arr[:middy])
    end = merge_sort(arr[middy:])

    return merge(start, end)

arrsfd = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(merge_sort(arrsfd))

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
