# 1503. Last Moment Before All Ants Fall Out of a Plank
# https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/description/

# Date: Aug 19, 2024
# Difficulty: Medium

# Solution
class Solution(object):
    def getLastMoment(self, n, left, right):
        """
        :type n: int
        :type left: List[int]
        :type right: List[int]
        :rtype: int
        """
        time = 0

        for l in left:
            time = max(time, l)
        
        for r in right:
            time = max(time, n - r)

        return time 