# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/

# Date: Nov 15, 2023
# Difficulty: Medium

# Time: O(n), Space: O(n)

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = []

        product = 1
        for i in range(n):
            result.append(product)
            product *= nums[i]

        product = 1
        for i in range(n-1, -1, -1):
            result[i] *= product
            product *= nums[i]

        return result


# Test case
solution = Solution()

nums = [-1,1,0,-3,3]
result = solution.productExceptSelf(nums)
print(result) # [0, 0, 9, 0, 0]