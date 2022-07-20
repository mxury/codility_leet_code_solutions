"""
Given an integer array nums, return the third distinct maximum number in this array.
If the third maximum does not exist, return the maximum number.
"""


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = list(set(nums))

        num.sort()

        if len(num) < 3:
            return num[-1]
        else:
            return num[-3]

test = [2,2,3,1]

print(Solution().thirdMax(test))