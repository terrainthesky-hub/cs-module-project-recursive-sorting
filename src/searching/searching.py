
# #find the middle

# #check if the target is above or below

# # // or use round() or math.floor()
# # math.ceil(5.5) = 6
# def binary_search(arr, target):
#     if len(arr) == 0:
#         return -1
#     #keep track of upper and lower bounds
#     low = 0
#     high = len(arr)-1
#     while low <= high:
#     #find the middle of those bounds
#         middle = (low + high) // 2 # // rounds to make sure it's an int

#         if target == arr[middle]:
#             return middle
            
#         #move upper or lower bound to the middle (to cut array in half)
#         ## depending on whether your above or below target
#         elif target > arr[middle]:
#             low = middle - 1
#         elif target < arr[middle]:
#             high = middle + 1 #rounding down makes this weird

#         #do it again

#         #stop if we have no values left

#     return -1


#move toward base case
## pass high and low as params

def binary_search(arr, target, low, high):
    middle = (low + high)//2
    #base case
    ## if our array is empty
    if len(arr) == 0:
        return -1
    # if low is gte high
    if low>= high:
        return -1

    if arr[middle] == target:
        return middle

    else:
        if target > arr[middle]:
            low = middle - 1 #get right of the right side

            #one_half = arr[middle:high + 1]

        elif target < arr[middle]:
            high = middle + 1 #get rid of the left side
            
            #one_half = arr[low:middle + 1]
            #remove low and high and change arr to one_half
    return binary_search(arr, target, low, high)

