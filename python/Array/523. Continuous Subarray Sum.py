# 523. Continuous Subarray Sum
# https://leetcode.com/problems/continuous-subarray-sum/

# Date: Sep 24, 2023
# Difficulty: Medium

# Solution
# Time: O(n), Space: O(n)
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        d = {0: -1} # make a dictionary that matches {residual : last index}
        subsum = 0

        for i, n in enumerate(nums):
            subsum = (subsum + n) % k

            if subsum not in d:
                d[subsum] = i
            else:
                if i - d[subsum] >= 2: # if the subarray is longer than 2, return True
                    return True
        return False

# Test case
solution = Solution()

nums = [23,2,4,6,7]
k = 6
result = solution.checkSubarraySum(nums, k)
print(result) # True