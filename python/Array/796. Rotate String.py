# 796. Rotate String
# https://leetcode.com/problems/rotate-string/

# Date: Nov 9, 2024
# Difficulty: Easy

# Solution 1: Queue rotate 
import collections
class Solution1(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        queue = collections.deque(s)

        for _ in range(len(s)):
            queue.rotate(1)
            if "".join(queue) == goal:
                return True
        return False

# Solution 2: concatenate string + string  
class Solution2(object):
    def rotateString(self, s, goal):
        if len(s) != len(goal):
            return False
        return goal in s + s
        

# Test case
solution = Solution1()
s = "abcde"; goal = "cdeab"
result = solution.rotateString(s, goal)
print(result) # true