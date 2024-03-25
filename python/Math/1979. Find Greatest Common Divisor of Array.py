# 1979. Find Greatest Common Divisor of Array
# https://leetcode.com/problems/find-greatest-common-divisor-of-array/description/

# Date: Sep 25, 2023
# Difficulty: Easy

# Time: O(n*log(n)), Space: O(n)
class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        smallest = min(nums)
        largest = max(nums)

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        if largest % smallest == 0:
            return smallest

        else:
            return gcd(largest, smallest)


# Test case
solution = Solution()

nums = [2,5,6,9,10]
result = solution.findGCD(nums)
print(result)