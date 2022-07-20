"""
Given a list of strings words and a string pattern, return a list of words[i] that match pattern.
 You may return the answer in any order.
A word matches the pattern if there exists a permutation of letters p so that after
replacing every letter x in the pattern with p(x), we get the desired word.
Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter,
and no two letters map to the same letter.
"""


class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        word_list = list()
        for word in words:
            perm_dict = {}
            pat_match = str()
            for i, letter in enumerate(word):
                if letter not in perm_dict.keys():
                    if pattern[i] not in perm_dict.values():
                        perm_dict[letter] = pattern[i]
                    else:
                        break
                pat_match += perm_dict[letter]

            if pat_match == pattern:
                word_list.append(word)

        return word_list



words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
pattern = "abb"

print(Solution().findAndReplacePattern(words, pattern))