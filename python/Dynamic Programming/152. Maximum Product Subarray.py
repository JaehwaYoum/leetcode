# 152. Maximum Product Subarray
# https://leetcode.com/problems/maximum-product-subarray/

# Date: March 25, 2024
# Difficulty: Medium

# Solution
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_prod = min_prod = result = nums[0]

        for num in nums[1:]:
            max_temp = max_prod * num
            min_temp = min_prod * num

            max_prod = max(max_temp, min_temp, num)
            min_prod = min(max_temp, min_temp, num)

            result = max(max_prod, result)

        return result


# Test case
solution = Solution()

nums = [2,3,-2,4]
result = solution.maxProduct(nums)

print(result) # 6
