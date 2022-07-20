"""
A parentheses string is valid if and only if:

    It is the empty string,
    It can be written as AB (A concatenated with B), where A and B are valid strings, or
    It can be written as (A), where A is a valid string.

You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

    For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a
    closing parenthesis to be "())))".

Return the minimum number of moves required to make s valid.
"""


class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        opened = list()
        bracket_dict = {")": "(", "}": "{", "]": "["}
        errors = 0
        for bracket in s:
            if bracket in bracket_dict.values():
                opened.append(bracket)

            elif bracket in bracket_dict.keys():
                if not opened:
                    errors += 1
                    continue
                if bracket_dict[bracket] != opened[-1]:
                    errors += 1
                else:
                    opened.pop(-1)

        return errors + len(opened)

s = ["())", '(((']
for brackets in s:
    print(Solution().minAddToMakeValid(brackets))

A = [0,1]
B = [1,0]

for a, b in zip(A,B):
    print(a,b)