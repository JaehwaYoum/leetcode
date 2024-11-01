# 1535. Find the Winner of an Array Game
# https://leetcode.com/problems/find-the-winner-of-an-array-game/description/

# Date: Nov 1, 2024
# Difficulty: Medium

# Solution
class Solution(object):
    def getWinner(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        winner = arr[0]
        count = 0

        if k >= len(arr):
            return max(arr)

        while count < k:
            first = arr[0]
            second = arr[1]

            if first > second:
                winner = first
                count += 1
                arr.append(second)
                arr.pop(1)
            else:
                winner = second
                count = 1
                arr.append(first)
                arr.pop(0)

        return winner

# Test case
solution = Solution()
arr = [2,1,3,5,4,6,7]; k = 2
result = solution.getWinner(arr, k)
print(result)