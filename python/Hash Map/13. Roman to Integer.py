# 13. Roman to Integer
# https://leetcode.com/problems/roman-to-integer/

# Date: Jan 24, 2025
# Difficulty: Easy

# Solution 1: Deque 
# Time: O(n), Space: O(n) 
class Solution1(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        import collections 
        queue = collections.deque(s)

        int_map = {"I":1, "V":5, "X": 10, "L":50, "C":100, "D":500, "M":1000}
        sub_map = {"IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}
        
        result = 0
        while len(queue) >= 2:
            first = queue.popleft()
            second = queue[0] 

            if (first + second) in sub_map:
                result += sub_map[first + second]
                queue.popleft()
            else:
                result += int_map[first]

        if queue:
            result += int_map[queue.popleft()]
        
        return result


# Solution 2: String Replacement 
# Time: O(n), Space: O(n) 
class Solution2(object):
    def romanToInt(self, s):
        char_map = {"I":1, "V":5, "X": 10, "L":50, "C":100, "D":500, "M":1000}
        result = 0

        s = s.replace("IV", "IIII").replace("IX", "VIIII") # replace creates new string copies 
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")

        for char in s:
            result += char_map[char]
        
        return result


# Solution 3: Subtraction 
# Time: O(n), Space: O(1) 
class Solution3(object):
    def romanToInt(self, s):
        char_map = {"I":1, "V":5, "X": 10, "L":50, "C":100, "D":500, "M":1000}
        result = 0

        for i in range(len(s)):
            if i < len(s) - 1 and char_map[s[i]] < char_map[s[i+1]]: # handle the last character
                result -= char_map[s[i]]
            else:
                result += char_map[s[i]]

        return result 


# Test case
solution = Solution()

s = "MCMXCIV"
result = solution.romanToInt(s)
print(result)  # 1994