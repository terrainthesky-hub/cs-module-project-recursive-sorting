# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    arrA_idx = 0
    arrB_idx = 0

    #loop over the merged_arr
    for idx in range(elements):

        #check if we are at the end of one of the arrays

        #if so, just use the other array
        if arrA_idx >= len(arrA):
            merged_arr[idx] = arrB[arrB_idx]

            arrB_idx += 1

        elif arrB_idx >= len(arrB):
            merged_arr[idx] = arrA[arrA_idx]

            arrA_idx += 1

    #compare the first element of each array
    # smaller element goes into merged array
        if arrA[arrA_idx] < arrB[arrB_idx]:
            merged_arr[idx] = arrA[arrA_idx]

            arrA_idx += 1

        else:
            merged_arr[idx] = arrB[arrB_idx]

            arrB_idx += 1



    # Your code here


    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
#base case

#
def merge_sort(arr):
    # Your code here
    #base case
    if len(arr) <= 1: 
        return arr
    else:
        mid = len(arr) // 2
        #recurse on the left half
        left = merge_sort(arr[:mid])
        #recurse on the right half
        right = merge_sort(arr[mid:])

        arr = merge(left, right)
        #put things back together: merge




    # beg = arr[0].index()
    # end = arr[-1].index()
    # mid = (beg + end)/2

    # if beg < end:
    #     merge_sort(beg, end)



    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# # In other words, your implementation should not allocate any additional lists 
# # or data structures; it can only re-use the memory it was given as input

#instead of new array, let's swap stuff
# (x,y = y,x)



def merge_in_place(arr, start, mid, end):
#     # Your code here
    start2 = mid + 1
    if (arr[mid] <= arr[start2]):
        return arr

    while start < mid and start2 < end:
        #what if start is < start2
        if arr[start] < arr[start2]:
            start += 1
        else:
            #save the second item and its index
            value = arr[start2]
            idx = start2

            # shift everything over
            while idx != start:
                #move left neighbor to the right one step
                arr[idx] = arr[idx - 1]
                idx -= 1
            #move the second item over
            arr[start] = value
            #update our coutners
            start += 1
            start2 += 1
            mid += 1

         

                


## recurse on left and right halves



def merge_sort_in_place(arr, left, right):

# What's our base case?
## if the right is less than the left
    if right <= left:
        return arr
    else:
        #find our middle
        middle = (right - left) // 2
        #recurse on left and right halves
        merge_sort_in_place(arr, left, middle)

        merge_sort_in_place(arr, middle + 1, right)

        merge_in_place(arr, left, middle, right)
