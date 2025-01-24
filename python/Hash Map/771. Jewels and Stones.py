# 771. Jewels and Stones
# https://leetcode.com/problems/jewels-and-stones/

# Date: Nov 1, 2023
# Difficulty: Easy

# Solution 1
import collections
class Solution1(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        freq = collections.defaultdict(int)
        count = 0

        for char in stones:
            freq[char] += 1

        for char in jewels:
            count += freq[char]

        return count

# Solution 2
class Solution2(object):
    def numJewelsInStones(self, jewels, stones):
        return sum(s in jewels for s in stones)

# Test case
solution = Solution1()
jewels = "aA"
stones = "aAAbbbb"
result = solution.numJewelsInStones(jewels, stones)
print(result) # 3

