"""
Implement strStr().
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.
"""


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        if needle not in haystack:
            return -1

        return haystack.index(needle)


haystack = 'hello'
needle = 'll'

print(Solution().strStr(haystack, needle))