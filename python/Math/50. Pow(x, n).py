# 50. Pow(x, n)
# https://leetcode.com/problems/powx-n/

# Date: Mar 30, 2024
# Difficulty: Easy

# Solution: recursive
class Solution(object):
	def myPow(self, x, n):
		"""
		:type x: float
		:type n: int
		:rtype: float
		"""

		if x == 0:
			return 0
		elif n == 0:
			return 1
		elif n < 0:
			return 1 / (x * self.myPow(x, -n-1))

		elif n % 2 == 0:
			return 1 / self.myPow(x, n//2)

		return x * self.myPow(x, n-1)


# Test case
solution = Solution()

x = 2.00000; n = -2
result = solution.myPow(x, n)

print(result) # 0.25
