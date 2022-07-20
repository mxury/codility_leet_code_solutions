"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        opened = list()
        bracket_dict = {")": "(", "}": "{", "]": "["}

        for bracket in s:
            if bracket in bracket_dict.values():
                opened.append(bracket)

            elif bracket in bracket_dict.keys():
                if not opened:
                    return False
                if bracket_dict[bracket] != opened[-1]:
                    return False
                else:
                    opened.pop(-1)

        if not opened:
            return True
        else:
            return False



test = ["(){}", "{{{}}", "}"]

print(Solution().isValid(test[2]))