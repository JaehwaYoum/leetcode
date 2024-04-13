# 204. Count Primes
# https://leetcode.com/problems/count-primes/description/

# Date: Apr 12, 2024
# Difficulty: Medium

# Solution
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        seen = [0] * n  # consider numbers up to n-1 (strictly less than n)
        result = 0

        for num in range(2, n):
            if seen[num]:
                continue
            result += 1

            for k in range(num * num, n, num):  # start marking at num**2
                seen[k] = 1

        return result


# Test case
solution = Solution()

n = 100
result = solution.countPrimes(n)
print(result) # 25