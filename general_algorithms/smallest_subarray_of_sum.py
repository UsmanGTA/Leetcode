#!/usr/bin/python3
import math

def smallest_subarray_with_given_sum(sum, arr):
	window_sum = 0
	window_start = 0
	min_len = math.inf

	for window_end in range(len(arr)):
		window_sum += arr[window_end]
		print(window_sum)

		while window_sum >= sum:
			print('entered with window_sum at', window_sum)
			min_len = min(min_len, window_end - window_start + 1)
			window_sum -= arr[window_end]
			window_start += 1
	
	if min_len == math.inf:
		return 0

	return min_len

def main():
	print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
	print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
	print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))

main()