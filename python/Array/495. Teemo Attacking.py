# 495. Teemo Attacking
# https://leetcode.com/problems/teemo-attacking/description/

# Date: Apr 12, 2024
# Difficulty: Easy

# Solution 1: brute-force, TLE
class Solution1(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """

        if (not timeSeries) or (duration == 0):
            return 0

        timeset = set(timeSeries)
        for time in timeSeries:
            for d in range(duration):
                timeset.add(time + d)

        return len(timeset)

# Solution 2
class Solution2(object):
    def findPoisonedDuration(self, timeSeries, duration):
        if (not timeSeries) or (duration == 0):
            return 0

        result = 0

        for i in range(len(timeSeries) - 1):
            time = min(duration, timeSeries[i] - timeSeries[i-1])
            result += time

        result += duration # last poision
        return result


# Test case
solution = Solution2()

timeSeries = [1,2]
duration = 2

result = solution.findPoisonedDuration(timeSeries, duration)
print(result) # 3