# 219. Contains Duplicate II
# https://leetcode.com/problems/contains-duplicate-ii/description/

# Date: Jan 27, 2024
# Difficulty: Easy

# Solution
# Time: O(n), Space: O(n)
import collections
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        # initiate a default dict that stores the indices for each number
        result = collections.defaultdict(list)

        for i in range(len(nums)):
            # check if there is a duplicate & the difference of the indices
            if result[nums[i]] and i - result[nums[i]][-1] <= k:
                return True

            # if not, append the index
            result[nums[i]].append(i)

        return False

# Test case
solution = Solution()

nums = [1, 2, 3, 1, 2, 3]
k = 2
result = solution.containsNearbyDuplicate(nums, k)
print(result) # 4