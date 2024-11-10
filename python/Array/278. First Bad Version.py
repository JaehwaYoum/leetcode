# 278. First Bad Version
# https://leetcode.com/problems/first-bad-version/description/

# Date: Nov 9, 2024
# Difficulty: Easy

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n # 1-based indexing problem

        while left < right:
            mid = left + (right - left) //2 

            if isBadVersion(mid):
                right = mid 
            else:
                left = mid + 1 

        return left

def isBadVersion(x):
    return x == bad

# Test case
solution = Solution()
n = 5; bad = 4
result = solution.firstBadVersion(n)
print(result)