#!/usr/bin/python3

def max_sub_array_of_size_k(k, arr):
    """
    -------------------------------
    METHOD: max_sub_array_of_size_k
    -------------------------------
    Description:
        Finds a subarray of k items
        that when added together,
        generate the largest sum
    Args:
        @k: size of the sub-array to check
        @array: array input
    Return:
        Return the largest sum
    """
    window_sum = 0                  # Stores the total of the arrays in the current window
    max_sum = 0                     # Store the max found so far
    start = 0                       # acts as the beginning index

    for end in range(len(arr)):
        window_sum += arr[end]
        if end >= k-1:
            max_sum = max(window_sum, max_sum)
            window_sum -= arr[start]                # Remove the beginning element in the subarray
            start += 1                              # increment start += 1 for the next loop

    return max_sum


# Test cases
cases = {'3': [2, 1, 5, 1, 3, 2],                   # Good test case
         '2': [2, 3, 4, 1, 5],                      # Another good test case
         '1': [2, 3, 4, 1, 5],                      # Testing if it could find 1 max
         '4': [2, 3] }                              # test if k's bigger than len(arr)

for k, arr in cases.items():
    print('Window size = ', k, 'array =', arr, 'Final return', max_sub_array_of_size_k(int(k), arr))
