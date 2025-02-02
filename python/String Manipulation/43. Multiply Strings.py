# 43. Multiply Strings
# https://leetcode.com/problems/multiply-strings/

# Date: Jan 27, 2025
# Difficulty: Medium

# Solution 1: Carry multiplication 
# Time: O(n * m), Space: O(1)
class Solution1(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n, m = len(num1), len(num2)
        result, carry1 = 0, 1

        for i in range(n):
            carry2 = 1
            for j in range(m):
                result += int(num1[i]) * int(num2[j]) * carry1 * carry2
                # result += int(num1[i]) * int(num2[j]) * 10**(i+j) -- TLE: exponential power calculations inefficient
                carry2 *= 10
            carry1 *=10

        return str(result)



# Solution 2: ord() digit conversion 
# Time: O(n), Space: O(n)
class Solution2(object):
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"

        n, m = len(num1), len(num2)
        result = [0] * (n + m)

        for i in range(n-1, -1, -1):
            carry = 0 # reset carry for every i 
            for j in range(m-1, -1, -1):
                digit1 = ord(num1[i]) - ord("0")
                digit2 = ord(num2[j]) - ord("0")
                
                temp = digit1 * digit2 + carry + result[i+j+1]
                result[i+j+1] = temp % 10
                carry = temp // 10
            result[i] += carry # add remaining carry 

        return "".join(map(str, result)).lstrip("0")

        # i = 0
        # while i < len(result) and result[i] == 0:
        #     i += 1
        # return "".join(map(str, result[i:]))


# Test case
solution = Solution1()

num1 = "123"; num2 = "456"
result = solution.multiply(num1, num2)
print(result) # "56088"
