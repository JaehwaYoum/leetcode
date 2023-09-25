# 27. Remove Element.py
# https://leetcode.com/problems/remove-element/

# Date: Jul 02, 2023
# Difficulty: Easy

# Time: O(n)
# Space: O(1)

# Solution 1
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k

# Test case
solution = Solution()

nums = [0,1,2,2,3,0,4,2]
val = 2
result = solution.removeElement(nums, val)
print(result) # 5