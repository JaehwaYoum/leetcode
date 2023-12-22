# 179. Largest Number
# https://leetcode.com/problems/largest-number/

# Date: Nov 28, 2023
# Difficulty: Medium

# Solution
class Solution(object):
    @staticmethod
    def to_swap(n1, n2):
        return str(n1) + str(n2) < str(n2) + str(n1)

    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        i = 1
        while i < len(nums):
            j = i
            while j > 0 and self.to_swap(nums[j - 1], nums[j]):
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
                j -= 1
            i += 1

        return str(int(''.join(map(str, nums))))


# Test case
solution = Solution()

nums = [3,30,34,5,9]
result = solution.largestNumber(nums)
print(result) # 9534330
