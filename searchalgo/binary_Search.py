# ---------- Binary Search -------------

# ------ input ------
# [2,4,7,10,13]
# number guessed ==== 10

# --------  Output --------
# position 3

def BinarySearch(array, item):
    low = 0
    hi = int(len(array))-1
    mid_value = (hi + low)/2
    cond = True
    while cond:
        hi = 0
        low = len(array)-1
        mid_value = int((hi + low)/2)
        if array[mid_value] == item:
            print(mid_value)
            cond = False
        elif array[mid_value] < item:
            hi = mid_value - 1
            print("second case")
        elif array[mid_value] > item:
            low = mid_value + 1
            print("third case")
        else:
            print('not here')


# rray = [2, 4, 5, 6]

# hi = 0
# low = int(len(array))-1

# print(array[mid_value])

def BinarySearch(array, item):
    low = 0
    # hi = int(len(array))-1
    high = len(array)
    for i in range(low, high):
        print(f'for low {low}', f' for high {high}')
        mid_value = int((high + low)/2)
        print(mid_value)
        print(low, high)
        if array[mid_value] == item:
            print("first case", array[mid_value])
            print("INDEX", mid_value)

            return mid_value
        elif array[mid_value] > item:
            high = mid_value
            print(array[mid_value])
            print("second case")
            # print("second case", newarr)
            # hi = hi
            # newarr = array[low:mid_value]

            # BinarySearch(newarr, item)
        elif array[mid_value] < item:
            low = mid_value
            print(low)
            print(array[mid_value])
            # newarr = array[mid_value:hi+1]
            print("third case")
            # BinarySearch(newarr, item)


BinarySearch([2, 4, 7, 8, 9, 10, 11, 13, 14, 17], 11)
