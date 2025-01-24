# 128. Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/description/

# Date: Feb 9, 2024
# Difficulty: Medium

# Solution 1: Dynamic Programming
class Solution1(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums = sorted(nums)

        dp = {} # default dict
        result = 0

        for num in nums:
            # update dp with the dictionary value of num-1 or 0, incremented by 1
            dp[num] = dp.get(num - 1, 0) + 1
            result = max(result, dp[num])

        return result

# Solution 2: Hash set
class Solution2(object):
    def longestConsecutive(self, nums):
        nums_set, result = set(nums), 0

        for num in nums_set:
            if num - 1 in nums_set:
                continue

            i = 1
            while num + i in nums_set:
                i += 1
                result = max(result, i)

        return result



# Test case
solution = Solution2()

nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
result = solution.longestConsecutive(nums)
print(result)  # 9


