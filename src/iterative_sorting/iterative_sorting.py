# SELECTION - SORT
def selection_sort( arr ):
    for i in range(0, len(arr) - 1):
        cur_index = i
        min_index = cur_index

        for j in range(i, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index], arr[cur_index] = arr[cur_index], arr[min_index]
    return arr


# BUBBLE - SORT
def bubble_sort( arr ):
    int = 0
    while int <= (len(arr)-1):
        print(int)
        for i in range(0, (len(arr)-1)):
            if arr[i] > arr[i + 1] and arr[i] != arr[len(arr)-1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        int+=1
    return arr


# COUNT - SORT
def count_sort( arr, maximum=-1 ):
    # not sure if I was supposed to do this, but no range was provided in tests and one of the tests was providing random values...
    # count needs to know the range of values to be efficient
    highest = 0
    for item in arr:
        if item > highest:
            highest = item

    if len(arr) == 0:
        return arr

    count_arr = [0] * (highest + 1)

    for i in arr:
        if i < 0:
            return 'Error, negative numbers not allowed in Count Sort'
        count_arr[i] = count_arr[i] + 1

    int = 0
    for j in range(len(count_arr)):
        while count_arr[j] > 0:
            arr[int] = j
            int = int+1
            count_arr[j] = count_arr[j] - 1
    return arr
