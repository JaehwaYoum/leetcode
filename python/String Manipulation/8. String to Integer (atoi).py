# 8. String to Integer (atoi)
# https://leetcode.com/problems/string-to-integer-atoi/

# Date: Nov 9, 2024
# Difficulty: Medium

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip()
        neg_flag = False
        result = []

        if s[0] in "+-":
            if s[0] == '-':
                neg_flag = True
            s = s[1:]

        for c in s:
            if c.isdigit():
                result.append(c)
            else:
                break

        if not result:
            return 0

        result = int("".join(result))

        if neg_flag:
            result *= -1 

        MIN, MAX = -2**31, 2**31 -1
        if result < MIN:
            return MIN
        elif result > MAX:
            return MAX
        else:
            return result



# Test case
solution = Solution()

s = " -042"
s = "1337c0d3"
result = solution.myAtoi(s)
print(result)