def cycle_sort(arr):
    writes = 0
    length_of_array = len(arr)

    # loop through the array to find cycles to rotate

    for i in range(0, (length_of_array - 1)):
        key      = arr[i]
        # Find where to put the item
        position = i
        for j in range(i+1, length_of_array):

            if arr[j] < key:
                position += 1
        # If the item is already there, this is not a cycle
        if position == i:
            continue

        # Otherwise, put the item there or right after any duplicates.
        while key == arr[position]:
            position += 1
        arr[position], key = key, arr[position]
        writes += 1

        # Rotate the rest of the cycle
        while position != i:

            # Find where to put the item
            position = i
            for j in range(i+1, length_of_array):
                if arr[j] < key:
                    position += 1

            # Put the item or right after any duplicates
            while key == arr[position]:
                position += 1
            arr[position], key = key, arr[position]
            writes += 1

    return writes

def print_array(arr):
    for i in range(len(arr)):
        print(arr[i], end = "  ")
    print()

# driver code
if __name__ == '__main__':
    arr = [1, 8, 3, 9, 10, 2, 10, 4]
    length_of_array = len(arr)

    print("Before Sorting:")
    print_array(arr)

    cycle_sort(arr)

    print("After Cycle Sorting :")
    print_array(arr)