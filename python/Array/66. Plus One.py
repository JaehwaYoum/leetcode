# 66. Plus One
# https://leetcode.com/problems/plus-one/

# Date: Oct 11, 2024
# Difficulty: Easy

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits

        return [1] + digits
# Test case
solution = Solution()
digits = [9, 9, 9]
result = solution.plusOne(digits)
print(result) # [1, 0, 0, 0]