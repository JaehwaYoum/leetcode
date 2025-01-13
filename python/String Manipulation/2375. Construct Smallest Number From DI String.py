# 2375. Construct Smallest Number From DI String
# https://leetcode.com/problems/construct-smallest-number-from-di-string/ 

# Date: Jan 5, 2025
# Difficulty: Medium


# Solution 1: slicing and reversing 
# Time: O(n), Space: O(n)
class Solution1(object):
    def smallestNumber(self, pattern):
        """
        :type pattern: str
        :rtype: str
        """
        n = len(pattern) + 1
        string = [str(i+1) for i in range(n)]
        start = 0
        result = []

        for k in map(len, pattern.split("I")):
            length = k + 1
            result[start: start+length] = string[start: start+length][::-1]
            start += length

        return "".join(result)

# Solution 2: stack
# Time: O(n), Space: O(n)
class Solution2(object):
    def smallestNumber(self, pattern):
        res = ""
        stack = []
        n = 1

        for i in range(len(pattern)):
            if pattern[i] == 'I':
                stack.append(n)
                n += 1
                while(stack):
                    char = stack.pop()
                    res += str(char)
            else:
                stack.append(n)
                n += 1
        stack.append(n)

        while stack:
            char = stack.pop()
            res += str(char)

        return res


# Test case
solution = Solution2()

pattern = "IIIDIDDD"
result = solution.smallestNumber(pattern)
print(result) # "123549876"