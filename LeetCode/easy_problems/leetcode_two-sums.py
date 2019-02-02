class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}

        for i in range(len(nums)):
            delta = target - nums[i]

            if delta in nums_dict:
                return [nums_dict[delta], i]

            nums_dict[nums[i]] = i

        return 'No two numbers found in the list that satisfy the target'

# test cases
# solution = Solution()
#
# nums = [2, 3, 5, 7]
# target = 9
# solution.twoSum(nums, target)
#
# nums = [3, 2, 4]
# target = 6
# solution.twoSum(nums, target)
#
# nums = [3, 3]
# target = 6
# solution.twoSum(nums, target)
#
