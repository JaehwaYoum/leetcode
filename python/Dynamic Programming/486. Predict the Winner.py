# 486. Predict the Winner
# https://leetcode.com/problems/predict-the-winner/description/

# Date: Jan 27, 2024
# Difficulty: Medium

class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        n = len(nums)
        dp = [[None for _ in range(n)] for _ in range(n)]

        def score(start, end):
            if dp[start][end] is not None:
                return dp[start][end]

            if start == end:
                dp[start][end] = nums[start]
                return dp[start][end]

            # based on the first player's choice, recursively call the score function for the opponent
            chooseStart  = nums[start] - score(start+1, end)
            chooseEnd = nums[end] - score(start, end-1)

            dp[start][end] = max(chooseStart, chooseEnd)
            return dp[start][end]


        # if the length is even, both player have equal turns and the first can always ensure at least a tie
        # if the length is odd, calculate the score for player 1 and check for at least a tie
        return len(nums) % 2 == 0 or score(0, len(nums) - 1) >= 0


# Test case
solution = Solution()

nums = [1, 5, 233, 7]
result = solution.predictTheWinner(nums)
print(result) # True