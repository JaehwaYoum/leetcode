# 371. Sum of Two Integers
# https://leetcode.com/problems/sum-of-two-integers/

# Date: Nov 15, 2023
# Difficulty: Medium

# Solution 1: Full adder
# Time: , Space:
class Solution1(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MASK = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFFF

        a_bin = bin(a & MASK)[2:].zfill(32)
        b_bin = bin(b & MASK)[2:].zfill(32)

        result = []
        carry = 0
        sum = 0

        for i in range(32):
            A = int(a_bin[31 - i])
            B = int(b_bin[31 - i])

            Q1 = A & B
            Q2 = A ^ B
            Q3 = carry & Q2
            sum = carry ^ Q2
            carry = Q1 | Q3

            result.append(str(sum))

        if carry == 1:
            result.append('1')

        result = int(''.join(result[::-1]), 2) & MASK

        if result > INT_MAX:
            result = ~(result ^ MASK)

        return result

# Solution 2: Simpler code
# Time: , Space:
class Solution2(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MASK = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFFF

        while b != 0:
            # addition and carry
            # & MASK ensures the results are constrained to a 32-bit range
            a, b = (a^b) & MASK, ((a&b)<<1) & MASK

        if a >INT_MAX:
            a = ~(a ^ MASK)

        return a

# Test case
solution = Solution2()

a = 1; b = 2
result = solution.getSum(a,b)
print(result) # 3



