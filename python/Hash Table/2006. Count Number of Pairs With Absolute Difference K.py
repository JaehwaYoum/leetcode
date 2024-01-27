# 2006. Count Number of Pairs With Absolute Difference K
# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/description/

# Date: Jan 27, 2024
# Difficulty: Easy

# Solution 1
# Time: O(n), Space: O(n)
import collections
class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        counter = collections.Counter(nums)
        result = 0

        for num in counter:
            if num + k in counter:
                result += counter[num] * counter[num + k]

        return result

# Test case
solution = Solution()

nums = [3,2,1,5,4]
k = 2
result = solution.countKDifference(nums, k)
print(result) # 3