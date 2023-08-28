# 287. Find the Duplicate Number
# https://leetcode.com/problems/find-the-duplicate-number/description/

# Date: Jul 10, 2023
# Difficulty: Medium

# Time: O(n)
# Space: O(n)

# Solution 1
class Solution(object):
    def findDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return num
            else:
                seen.add(num)

# Test case
solution = Solution()

nums = [1,3,4,2,2]
result = solution.findDuplicate(nums)
print(result)
# 2