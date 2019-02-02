from collections import Counter

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_dict = Counter(s)

        for char, char_count in char_dict.items():
            if char_count == 1:
                return s.index(char)

        return -1


# test cases
# solution = Solution()
#
# s = 'leetcode'
# solution.firstUniqChar(s)
#
# s = 'loveleetcode'
# solution.firstUniqChar(s)
