# 647. Palindromic Substrings
# https://leetcode.com/problems/palindromic-substrings/description/

# Date: Jan 5, 2025
# Difficulty: Easy


# Solution 1: Brute Force
# Time: O(n^3), Space: O(n)
class Solution1(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        
        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i:j+1]
                if substring == substring[::-1]:
                    result += 1
        return result


# Solution 2: Expand around center 
# Time: O(n^2), Space: O(1)
class Solution2(object):
    def countSubstrings(self, s):
        result = 0
        
        def palindrome_count(left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

        for i in range(len(s)):
            result += palindrome_count(i, i)
            result += palindrome_count(i, i+1)

        return result 


# Solution 3: Dynamic Programming
# Time: O(n^2), Space: O(n^2)
class Solution3(object):
    def countSubstrings(self, s):
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        result = 0

        for i in range(n):
            dp[i][i] = 1
            result += 1

        for i in range(n-1):
            dp[i][i+1] = 1 if s[i] == s[i+1] else 0
            if dp[i][i+1] == 1:
                result += 1

        for length in range(3, n+1):
            for i in range(n - length + 1): # starting index 
                j = i + length - 1 # ending index 
                dp[i][j] = (dp[i+1][j-1] == 1) and (s[i] == s[j])
                if dp[i][j] == 1:
                    result += 1

        return result


# Test case
solution = Solution3()

s = "aaa"
result = solution.countSubstrings(s)
print(result) # 6