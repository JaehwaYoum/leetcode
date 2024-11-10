# 7. Reverse Integer
# https://leetcode.com/problems/reverse-integer/description/

# Date: Nov 9, 2024
# Difficulty: Medium

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        string = str(x)

        if string[0] == '-':
            neg_flag = True
            string = string[1:]
        else:
            neg_flag = False

        string = string[::-1]

        if neg_flag:
            result = -int(string)
        else:
            result = int(string)

        # handle the 64-bit integers (signed or unsigned)
        if x < -2**63 or x > 2**63 -1:
            return 0

        return result


# Test case
solution = Solution()

x = -123
result = solution.reverse(x)
print(result)