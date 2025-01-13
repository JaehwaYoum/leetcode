# 7. Reverse Integer
# https://leetcode.com/problems/reverse-integer/description/

# Date: Nov 9, 2024
# Difficulty: Medium

# Solution 1: String conversion
# Time: O(n), Space: O(n)
class Solution1(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        string = str(x) # string conversion O(n)

        if string[0] == '-':
            neg_flag = True
            string = string[1:] # slicing O(n)
        else:
            neg_flag = False

        string = string[::-1]

        if neg_flag:
            result = -int(string)
        else:
            result = int(string) # integer conversion O(n)

        # handle the 64-bit integers (signed or unsigned)
        if x < -2**63 or x > 2**63 -1:
            return 0

        return result


# Solution 2: Digit-wise Reversal
# Time: O(n), Space: O(1)
class Solution2(object):
    def reverse(self, x):
        sign = [1, -1][x < 0] # One-liner: if false(0) then 1, else true(1) then -1
        rev, x = 0, abs(x)

        while x:
            x, mod = divmod(x, 10)
            rev = rev * 10 + mod

            if rev > 2**31 -1: # handle overflow
                return 0

        return sign * rev


# Test case
solution = Solution2()

x = -123
result = solution.reverse(x)
print(result)