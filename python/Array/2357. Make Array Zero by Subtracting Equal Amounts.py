# 2357. Make Array Zero by Subtracting Equal Amounts
# https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/description/

# Date: Feb 9, 2024
# Difficulty: Easy


# Solution
class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        counter = Counter(nums)
        if 0 in counter.keys():
            counter.pop(0)
        return len(counter)

# Test case
solution = Solution()

nums = [1,5,0,3,5]
result = solution.minimumOperations(nums)
print(result) # 3