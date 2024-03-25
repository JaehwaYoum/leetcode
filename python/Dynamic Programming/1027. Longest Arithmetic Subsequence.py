# 1027. Longest Arithmetic Subsequence
# https://leetcode.com/problems/longest-arithmetic-subsequence/description/

# Date: Feb 9, 2024
# Difficulty: Easy

# Solution
class Solution(object):
    def longestArithSeqLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        dp = [{} for _ in range(len(nums))]
        result = 0
        
        for i in range(len(nums)):
            dp[i][0] = 1

            for j in range(i):
                diff = nums[i] - nums[j]
            
                if diff in dp[j]:
                    dp[i][diff] = dp[j][diff] + 1
                else:
                    dp[i][diff] = 2
            
            result = max(result, max(dp[i].values()))

        return result

# Test case
solution = Solution()

nums = [20,1,15,3,10,5,8]
result = solution.longestArithSeqLength(nums)
print(result) # 4