# 1010. Pairs of Songs With Total Durations Divisible by 60
# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/description/

# Date: Feb 9, 2024
# Difficulty: Medium

# Solution
class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        
        counter = [0] * 60
        result = 0

        for t in time:
            counter[t % 60] += 1
        
        for i in range (1, 30):
            result += counter[i] * counter[60 - i]
        
        result += counter[0] * (counter[0] - 1) // 2
        result += counter[30] * (counter[30] - 1) // 2

        return result


# Test case
solution = Solution()
time = [30,20,150,100,40]
result = solution.numPairsDivisibleBy60(time)
print(result) # 3