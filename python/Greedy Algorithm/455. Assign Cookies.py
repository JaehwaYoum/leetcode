# 455. Assign Cookies
# https://leetcode.com/problems/assign-cookies/

# Date: Dec 23, 2023
# Difficulty: Easy

# Solution 1: Greedy algorithm
class Solution1(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """

        # sort the child and cookie lists to be ascending
        g.sort()
        s.sort()

        child_index, cookie_index = 0, 0

        while child_index < len(g) and cookie_index < len(s):
            if s[cookie_index] >= g[child_index]:
                child_index += 1 # assign the cookie to the child
            cookie_index += 1 # move on to check for the next cookie

        return child_index

# Solution 2: Binary search
import bisect
class Solution2(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()

        result = 0
        for i in s:
            index = bisect.bisect_right(g, i) # search from the right (to ensure cookie is larger)
            if index > result:
                result += 1 # update to retrieve the largest result
        return result

# Test case
solution = Solution2()
g = [1,2]; s = [1,2,3]
result = solution.findContentChildren(g, s)
print(result) # 2