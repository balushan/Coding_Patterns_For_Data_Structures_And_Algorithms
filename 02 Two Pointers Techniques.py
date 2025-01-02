# Check if any pair exist in the list whose sum is equal to the target value
def two_sum(arry, target):

    arry.sort()  # Sort the array

    left = 0
    right = len(arry) - 1
    while left < right:
        summation = arry[left] + arry[right]
#        print('summation = ', summation, 'target = ', target)
        if summation == target:
            print('left =', left, ' arr[left]=', arry[left], ' right=', right, ' arr[right]=', arry[right])
            return True
        if summation < target:
            left += 1
        else:
            right -= 1
    # No pair is found
    return False


def print_array(ar):
    for i in range(len(ar)):
        print(ar[i], end=" ")
    print()


# driver code
if __name__ == '__main__':
    # arr, target = [1, 2, 3, 4, 6], 6
    # arr, target = [2, 5, 9, 11], 11
    # arr, target = [2, 7, 11, 15], 9
    # arr, target = [3, 2, 4], 6
    # arr, target = [3, 3], 6
    arr, target = [0, -1, 2, -3, 1], -2

    print("Original Array List :", end=" ")
    print_array(arr)
    print("Sum of the target is:", target)

    if two_sum(arr, target):
        print("True")
    else:
        print("False")
