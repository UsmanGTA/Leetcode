#!/usr/bin/python3

class Solution:
    def twoSum(self, nums, target):
        """
        --------------
        METHOD: TwoSum
        --------------
        Description:
            Method that returns two indexes
            that when added together return
            the target.
            This task was pulled from Leetcode:
            https://leetcode.com/problems/two-sum/submissions/
        Args:
            @nums: list of integers
            @target: number required after summed
        """
        mapper = {}

        for index, number in enumerate(nums):
            diff = target - number
            if number in mapper:
                return [mapper[number], index]
            else:
                mapper[diff] = index
