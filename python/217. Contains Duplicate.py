# 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/

# Date: Jul 19, 2023
# Difficulty: Easy

# Time: O(n), Space: O(n)
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        unique = set(nums)
        if len(unique) == len(nums):
            return False
        else:
            return True


# Test case
solution = Solution()

nums = [1,1,1,3,3,4,3,2,4,2]
result = solution.containsDuplicate(nums)
print(result) # True