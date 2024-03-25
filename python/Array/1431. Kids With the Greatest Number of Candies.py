# 1431. Kids With the Greatest Number of Candies
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

# Date: Feb 25, 2024
# Difficulty: Easy

# Solution
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        
        value = max(candies) - extraCandies
        return [candy>=value for candy in candies]

# Test case
solution = Solution()
candies = [2,3,5,1,3]; extraCandies = 3
result = solution.kidsWithCandies(candies, extraCandies)
print(result) # [true,true,true,false,true] 
