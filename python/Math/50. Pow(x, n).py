# 50. Pow(x, n)
# https://leetcode.com/problems/powx-n/

# Date: Mar 30, 2024
# Difficulty: Easy

# Solution 1: recursive
# odd n -> Time: O(n), Space: O(n)
# even n -> Time: O(log n), Space: O(log n)
class Solution1(object):
	def myPow(self, x, n):
		"""
		:type x: float
		:type n: int
		:rtype: float
		"""
		if n == 0:
			return 1
		elif n < 0:
			return 1 / self.myPow(x, -n)
		elif n % 2 == 0:
			return 1 / self.myPow(x, n//2)

		return x * self.myPow(x, n-1)


# Solution 2: recursive (enhanced)
# Time: O(log n), Space: O(log n)
class Solution2(object):
	def myPow(self, x, n):
		if n == 0:
			return 1
		elif n < 0:
			return 1 / self.myPow(x, -n)

		half = self.myPow(x, n//2)
		if n % 2 == 0:
			return half * half
		else:
			return x * half * half


# Solution 3: Bitwise Manipulation 
# Time: O(log n), Space: O(1)
class Solution3(object):
	def myPow(self, x, n):
		if n < 0:
			x = 1 / x
			n *= -1

		result = 1
		while n:
			if n & 1: 	# n is odd
				result *= x
			x *= x 		# x = x ** 2
			n >>= 1 	# n = n // 2

		return result 


# Test case
solution = Solution3()

x = 2.00000; n = -2
result = solution.myPow(x, n)

print(result) # 0.25
