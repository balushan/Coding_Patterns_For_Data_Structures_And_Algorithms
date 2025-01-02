# maximum sum of a sub array of size k
def sub_array_max_sum(arr, k):
    length_of_array = len(arr)  # Length of the array

    if length_of_array < k:  # Check if the length of the array is smaller than sub array
        print('Array size is smaller than sub array. Invalid Sub Array Size')
        return -1

    window_sum = sum(arr[:k])  # Find the sum of first window of subarray size
    #    window_sum = sum([arr[i] for i in range(k)])   # Alternate way to sum the first array size (previous line)
    max_sum = window_sum  # assume the sum of first sub array is maximum

    # Finding the sum of remaining windows by
    # removing first elements of previous index
    # adding the last element of current window

    for i in range(length_of_array - k):  # loop the array
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(window_sum, max_sum)
    return max_sum


def print_array(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# Driver Code
if __name__ == '__main__':
    arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
    sub_array_size = 4

    print('Original Array List :', end=" ")
    print_array(arr)

    result = sub_array_max_sum(arr, sub_array_size)

    print('maximum sum of a  subarray of size ', sub_array_size, ' is: ', result)
