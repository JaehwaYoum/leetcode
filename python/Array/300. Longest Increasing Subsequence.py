# 300. Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/description/

# Date: Feb 9, 2024
# Difficulty: Medium

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tails = [0] * len(nums)
        result = 0

        for num in nums:
            i, j = 0, result
            while i != j:
                m = (i + j) // 2

                if tails[m] < num:
                    i = m + 1
                else:
                    j = m

            tails[i] = num
            result = max(i + 1, result)

        return result

# Test case : in-place without making a copy of the array.
solution = Solution()

nums = [10,9,2,5,3,7,101,18]
result = solution.lengthOfLIS(nums)
print(result) # 4

# Interim results
# each position i in tails represents an increasing subsequence of length i+1
# with the smallest possible ending value found so far.
"""
Process 10
tails becomes [10, 0, 0, 0, 0, 0, 0, 0], result becomes 1.
Process 9
tails is updated to [9, 0, 0, 0, 0, 0, 0, 0], result remains 1.
Process 2
tails is updated to [2, 0, 0, 0, 0, 0, 0, 0], result remains 1.
Process 5
tails is updated to [2, 5, 0, 0, 0, 0, 0, 0], result becomes 2.
Process 3
tails is updated to [2, 3, 0, 0, 0, 0, 0, 0], result remains 2.
Process 7
tails is updated to [2, 3, 7, 0, 0, 0, 0, 0], result becomes 3.
Process 101
tails is updated to [2, 3, 7, 101, 0, 0, 0, 0], result becomes 4.
Process 18
tails is updated to [2, 3, 7, 18, 0, 0, 0, 0], result remains 4.
"""