"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        min_len = 200
        for st in strs:
            min_len = min(len(st), min_len)
        counter = 0
        for j in range(min_len):
            prefix = list()
            for st in strs:
                prefix.append(st[j])

            if len(set(prefix)) != 1:
                break
            else:
                counter += 1


        return strs[0][:counter]


test = ['hello','helbath']


sol = Solution()
print(sol.longestCommonPrefix(test))

