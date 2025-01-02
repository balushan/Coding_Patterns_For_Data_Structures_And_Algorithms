# Merge all the overlapping intervals into one and output mutually exclusive intervals
#Input: [[7, 8], [1, 5], [2, 4], [4, 6]]
#Output: [[1, 6], [7, 8]]

def merge_overlapping_intervals(data):

    data.sort()                 # Sort the array based on the starting values
    print(data)
    print(data[0])

    result = []                 # temporary array to store the merges intervals result
    result.append(data[0])

    for i in range(len(data)):
        current = data[i]
        last    = result[-1]

        print('last = ', last, ' current = ', current)

        # if the current intervals overlap last intervals, then merge them
        if current[0] <= last[1]:
            last[1]    = max(last[1], current[1])
        else:
            result.append(current)
    return result



# driver code
if __name__ == '__main__':
    arr = [[7,8], [1,5], [2,4], [4,6]]

    print('Original array :', end = " ")
    print(arr)

    res = merge_overlapping_intervals(arr)

    for interval in res:
        print(interval[0], interval[1])