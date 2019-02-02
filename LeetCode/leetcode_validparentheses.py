class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = s.replace(' ', '')

        # quick exit if the number of parentheses is not even
        if len(s) % 2 != 0:
            return False

        par_dict = {')': '(',
                    ']': '[',
                    '}': '{'}

        stack = []

        for par in s:
            if par in par_dict:
                compare = stack.pop() if stack else 'dummy'

                if compare != par_dict[par]:
                    return False

            else:
                stack.append(par)

        if len(stack) > 0:
            return False
        else:
            return True


# test cases
# s = '(((((((()'
# solution = Solution()
# solution.isValid(s)
