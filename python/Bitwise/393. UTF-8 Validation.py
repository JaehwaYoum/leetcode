# 393. UTF-8 Validation
# https://leetcode.com/problems/utf-8-validation/

# Date: Nov 22, 2023
# Difficulty: Medium

# Solution
# Time: O(n), Space: O(1)
class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        #  verify that the subsequent bytes all start with 10
        def check(size):
            for i in range(start + 1, start + size + 1):
                if i >= len(data) or (data[i] >> 6) != 0b10:
                    return False
            return True

        start = 0
        while start < len(data):
            first = data[start]
            if (first >> 3) == 0b11110 and check(3):
                start += 4
            elif (first >> 4) == 0b1110 and check(2):
                start += 3
            elif (first >> 5) == 0b110 and check(1):
                start += 2
            elif (first >> 7) == 0:
                start += 1
            else:
                return False
        return True


# Test case
solution = Solution()
data = [197, 130, 1]
result = solution.validUtf8(data)
print(result) # true