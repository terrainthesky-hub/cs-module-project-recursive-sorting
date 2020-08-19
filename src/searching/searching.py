# TO-DO: Implement a recursive implementation of binary search

#find the middle
#check if the target is above or below
#focus on one side or the other
def binary_search(arr, target):
    if len(arr) == 0:
    
    low = 0
    high = len(arr)-1

    return -1
    # Your code here
    # low = 0
    # high = len(arr) - 1

    # middle = (low + high) // 2
    # guess = arr[middle]
    # if guess == target:
    #     return middle
    # elif guess > target:
    #     high = middle - 1
    #     binary_search(high, target, start, end)
    # else:
    #     low = middle + 1
    #     binary_search(low, target, start, end)
    # return -1

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code her