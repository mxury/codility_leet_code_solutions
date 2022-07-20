"""
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.
A subarray is a contiguous part of an array.
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return sum(nums)
        # cumsum = [0]
        cumsum = list()
        sm = 0
        for num in nums:
            sm += num
            cumsum.append(sm)
        print(cumsum)
        return max(cumsum) - min(cumsum)


test = [[5,4,-1,7,8], [-2,1,-3,4,-1,2,1,-5,4],[-2,1]]

for t in test:
    print(Solution().maxSubArray(t))

