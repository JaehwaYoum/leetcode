# 1512. Number of Good Pairs
# https://leetcode.com/problems/number-of-good-pairs/description/

# Date: Jan 27, 2024
# Difficulty: Easy

# Solution: Counter
# Time: O(n), Space: O(k) (k: number of unique values in nums)
import collections
class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = collections.Counter(nums)
        count_list = [ int(value * (value - 1) / 2) for value in count.values()]
        return sum(count_list)

# Test case
solution = Solution()

nums = [1,2,3,1,1,3]
result = solution.numIdenticalPairs(nums)
print(result) # 4