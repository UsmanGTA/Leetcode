class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
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
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]
